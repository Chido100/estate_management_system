from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User, Profile
from .forms import RegisterResidentForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token



# Activation email
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Thank you for confirming your email. You can now login to your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid.")
    return redirect('login')

def activate_email(request, user, to_email):
    mail_subject = "Activate your account."
    message = render_to_string("users/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user}, please check your email {to_email} and click on the activation link to verify account.') 
    else:
        messages.error(request, f"There's been a problem sending email to {to_email}, please check that email address is correct.")




# Register a user
def register_resident(request):
    if request.method == "POST":
        form = RegisterResidentForm(request.POST)
        if form.is_valid():
            resident = form.save(commit=False)
            # Make is_resident true for newly registered user
            resident.is_resident = True
            resident.save()
            activate_email(request, resident, form.cleaned_data.get('email'))
            return redirect("login")
    else:
        form = RegisterResidentForm()
    return render(request, "users/register_resident.html", {'form': form})


# Register Resident pending approval
def pending_approval_page(request):
    return render(request, 'users/pending_approval_page.html')




# Resident Details
@login_required
def resident_details(request, pk):
    resident = get_object_or_404(User, pk=pk)
    return render(request, 'users/resident_details.html', {'resident': resident})




# View all residents
@login_required
def all_residents(request):
    residents = User.objects.all().order_by("-date_joined")
    paginator = Paginator(residents, 10)
    try:
        page_number = request.GET.get('page', 1)
        users = paginator.page(page_number)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    
    # Filter residents
    all_residents = User.objects.filter(is_resident=True)
    total_resident_users = all_residents.count()

    # Filter security team
    all_security = User.objects.filter(is_security=True)
    total_security_users = all_security.count()

    # Filter management team
    all_management = User.objects.filter(is_management=True)
    total_management_users = all_management.count()

    return render(request, 'users/all_residents.html', {
        'residents': residents,
        'users': users,
        'total_resident_users': total_resident_users,
        'total_security_users': total_security_users,
        'total_management_users': total_management_users
    })
    



# User profile
@login_required
def profile_view(request):
    template_name = 'users/profile.html'
    user_form_class = UserUpdateForm
    profile_form_class = ProfileUpdateForm

    u_form = user_form_class(instance=request.user)

    if hasattr(request.user, 'profile'):
        p_form = profile_form_class(instance=request.user.profile)
    else:
        p_form = profile_form_class()
    
    if request.method == 'POST':
        u_form = user_form_class(request.POST, instance=request.user)

        if hasattr(request.user, 'profile'):
            p_form = profile_form_class(request.POST, request.FILES, instance=request.user.profile)
        else:
            p_form = profile_form_class(request.POST, request.FILES)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()

            if not hasattr(request.user, 'profile'):
                profile = p_form.save(commit=False)
                profile.user = request.user
                profile.save()
            else:
                p_form.save()

            messages.info(request, 'Your account has been updated!')
            return redirect('profile')
    return render(request, template_name, {'u_form': u_form, 'p_form': p_form})



