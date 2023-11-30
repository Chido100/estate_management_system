from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User
from .forms import RegisterResidentForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


# Register a user
def register_resident(request):
    if request.methd == "POST":
        form = RegisterResidentForm(request.POST)
        if form.is_valid():
            resident = form.save(commit=False)
            resident.is_resident = True
            resident.save()
            messages.info(request, "Your account has been successfully resgistered!")
            return redirect("login")
        else:
            messages.warning(request, "Something went wrong. Please check your details and try again.")
            return redirect("register-resident")
    else:
        form = RegisterResidentForm()
    return render(request, "users/register_resident.html", {"form": form})


# View all residents
@login_required
def all_residents(request):
    residents = User.objects.all().order_by("-date_joined")
    return render(request, "users/all_residents.html", {"residents": residents})
    