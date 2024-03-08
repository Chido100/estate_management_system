from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CommunityMail
from .forms import CommunityMailForm



@login_required
def send_mail(request):
    if request.method == 'POST':
        form = CommunityMailForm(request.POST)
        if form.is_valid():
            mail = form.save(commit=False)
            mail.sender = request.user
            mail.save()
            username = form.cleaned_data.get('username')
            messages.info(request, f'Mail is successfully sent to {username}')
            return redirect('send-mail')
    else:
        form = CommunityMailForm()
    return render(request, 'community_mail/send_mail.html', {'form': form})


@login_required
def inbox(request):
    received_mail = CommunityMail.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'community_mail/inbox.html', {'received_mail': received_mail})

