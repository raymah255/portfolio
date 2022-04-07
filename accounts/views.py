from multiprocessing import context
from tkinter import EW
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def login_views(request, *args, **kwargs):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/feeds/")
    context={
            "form": form,
            "sub_label": "Login",
            "log_label": "Login User",
            "reg_lik": "/accounts/register"
        }
    return render(request, "accounts/login.html", context)


def register_views(request, *args, **kwargs):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            password = form.cleaned_data.get("password")
            user.set_password(password)
            return redirect("/accounts/login")
    context={
        "form": form,
        "sub_label": "Reister",
        "log_label": "Register User",
    }
    form = UserCreationForm()
    return render(request, "accounts/login.html", context)

def logout_views(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("/accounts/login")  
    context={
        "sub_label": "Logout",
        "log_label": "Logout User",
        "message": "Are you Sure wanna Logout ?" 
    }
        
    return render(request, "accounts/login.html", context)
