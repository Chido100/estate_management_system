from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import VisitorAccessRequest
from .forms import VisitorAccessRequestForm
from users.models import User
from django.contrib.auth.decorators import login_required
import datetime


# View Visitor Access details
@login_required
def access_request_details(request, pk):
    access_request = get_object_or_404(VisitorAccessRequest, pk=pk)

    va = User.objects.get(username=access_request.creator)
    va_per_user = va.creator.all()
    context = {'access_request': access_request, 'va_per_user': va_per_user}
    return render(request, 'visitor_access/visitor_access_details.html', context)



""" For Residents """

# Creating a Visitor Access request
@login_required
def create_access_request(request):
    if request.method == 'POST':
        form = VisitorAccessRequestForm(request.POST)
        if form.is_valid():
            va = form.save(commit=False)
            va.creator = request.user
            va.request_status = 'Pending'
            va.save()
            messages.info(request, "Your request has been successfully submitted.")
            return redirect('dashboard')
        else:
            messages.warning(request, "Something went wrong. Please check details.")
            return redirect('create-access-request')
    else:
        form = VisitorAccessRequest()
    return render(request, 'visitor_access/create_access_request.html', {'form': form})


# Update a Visitor Access request
@login_required
def update_access_request(request, pk):
    access_request = get_object_or_404(VisitorAccessRequest, pk=pk)
    if not access_request.is_resolved:

        if request.method == 'POST':
            form = VisitorAccessRequestForm(request.POST, instance=access_request)
            if form.is_valid():
                form.save()
                messages.info(request, "Your request has been updated and all changes are saved.")
                return redirect('dashboard')
            else:
                messages.warning(request, "Something went wrong. Please check details.")
        else:
            form = VisitorAccessRequestForm(instance=access_request)
            return render(request, 'visitor_access/update_access_request.html', {'form': form})

    else:
        messages.warning(request, "You cannot make any changes!")
        return redirect('dashboard')


# Viewing all created requests
@login_required
def all_access_requests(request):
    access_requests = VisitorAccessRequest.objects.filter(creator=request.user).order_by('-date_created')
    return render(request, 'visitor_access/all_access_requests.html', {'access_requests': access_requests})




""" For Security Team """


# View request queue
@login_required
def request_queue(request):
    access_request = VisitorAccessRequest.objects.filter(request_status='Pending')
    return render(request, 'visitor_access/request_queue.html', {'access_request': access_request})


# Accept a request from queue
@login_required
def accept_access_request(request, pk):
    access_request = VisitorAccessRequest.objects.get(pk=pk)
    access_request.assigned_to = request.user
    access_request.request_status = 'Active'
    access_request.accepted_date = datetime.datetime.now()
    access_request.save()
    messages.info(request, 'Access Request has been accepted, Please resolve as soon as possible.')
    return redirect('workspace')


# Close a request
@login_required
def close_access_request(request, pk):
    access_request = VisitorAccessRequest.objects.get(pk=pk)
    access_request.request_status = 'Completed'
    access_request.is_resolved = True
    access_request.closed_date = datetime.datetime.now()
    access_request.save()
    messages.info(request, 'Access Request has been resolved')
    return redirect('request_queue')


# Request security team is working on
@login_required
def workspace(request):
    access_requests = VisitorAccessRequest.objects.filter(assigned_to=request.user, is_resolved=False)
    return render(request, 'visitor_access/workspace.html', {'access_requests': access_requests})


# All closed/resolved requests
@login_required
def all_closed_requests(request):
    access_requests = VisitorAccessRequest.objects.filter(assigned_to=request.user, is_resolved=True)
    return render(request, 'visitor_access/all_closed_requests.html', {'access_requests': access_requests})
