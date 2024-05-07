from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Item
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
from users.models import User
from visitor_access.models import VisitorAccessRequest
from critical_alert.models import CriticalAlert
from incident_reporting.models import IncidentReporting
from django.utils import timezone



    
# Dashboard view
@login_required
def dashboard(request):
    items = Item.objects.filter(is_expired=False).order_by('-date_created')[:6]
    categories = Category.objects.all()

    # Dashboard charts details

    # All registered users
    all_resident_users = User.objects.filter(is_resident=True).count()
    security_team = User.objects.filter(is_security=True).count()
    management_team = User.objects.filter(is_management=True).count()

    # All visitor access requests
    today = timezone.now().date()
    all_new_visitor_access_request_today = VisitorAccessRequest.objects.filter(date_created__date=today).count()
    total_new_visitor_access_request = VisitorAccessRequest.objects.filter(request_status='Pending').count()
    all_active_visitor_access_request_today = VisitorAccessRequest.objects.filter(request_status='Active', date_created__date=today).count()
    total_active_visitor_access_request = VisitorAccessRequest.objects.filter(request_status='Active').count()
    all_completed_visitor_access_request_today = VisitorAccessRequest.objects.filter(request_status='Completed', date_created__date=today).count()
    total_completed_visitor_access_request = VisitorAccessRequest.objects.filter(request_status='Completed').count()

    # All critical alerts
    all_critical_alerts = CriticalAlert.objects.all().count()

    # All incident reports
    all_new_incident_reports_today = IncidentReporting.objects.filter(date_created__date=today).count()
    total_new_incident_reports = IncidentReporting.objects.filter(incident_status='Pending').count()
    all_active_incident_reports_today = IncidentReporting.objects.filter(incident_status='In-Progress', date_accepted__date=today).count()
    total_active_incident_reports = IncidentReporting.objects.filter(incident_status='In-Progress').count()
    all_completed_incident_reports_today = IncidentReporting.objects.filter(incident_status='Completed', date_closed__date=today).count()
    total_completed_incident_reports = IncidentReporting.objects.filter(incident_status='Completed').count()




    return render(request, 'dashboard/dashboard.html', {
        'items': items,
        'categories': categories,
        'all_resident_users': all_resident_users,
        'security_team': security_team,
        'management_team': management_team,
        'all_new_visitor_access_request_today': all_new_visitor_access_request_today,
        'total_new_visitor_access_request': total_new_visitor_access_request,
        'all_active_visitor_access_request_today': all_active_visitor_access_request_today,
        'total_active_visitor_access_request': total_active_visitor_access_request,
        'all_completed_visitor_access_request_today': all_completed_visitor_access_request_today,
        'total_completed_visitor_access_request': total_completed_visitor_access_request,
        'all_new_incident_reports_today': all_new_incident_reports_today,
        'total_new_incident_reports': total_new_incident_reports,
        'all_active_incident_reports_today': all_active_incident_reports_today,
        'total_active_incident_reports': total_active_incident_reports,
        'all_completed_incident_reports_today': all_completed_incident_reports_today,
        'total_completed_incident_reports': total_completed_incident_reports,
    })




# Item detail view
@login_required
def item_details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'dashboard/item_details.html', {'item': item})


# Add new item view
@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.creator = request.user
            item.save()
            return redirect('item-details', pk=item.id)
    else:
        form = NewItemForm()
    return render(request, 'dashboard/new_item.html', {'form': form, 'title': 'New Item'})




# Edit an item view
@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, creator=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item-details', pk=item.id)
    else:
        form = EditItemForm(instance=item)
    return render(request, 'dashboard/edit_item.html', {'form': form, 'title': 'Edit Item'})



# Delete an Item view
@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, creator=request.user)

    if request.method == 'POST':
        item.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/delete_item.html', {'item': item})

