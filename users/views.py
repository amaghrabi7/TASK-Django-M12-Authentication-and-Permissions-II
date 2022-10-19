from pdb import post_mortem
from django.shortcuts import render, redirect
from users.forms import UserRegister, LoginForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("home")
    context = {
        "form": form,
    }

    return render(request, "register.html", context)

def logout_user(request):
    logout(request)
    return redirect("login")


def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect("home")
    
    context = {
        "form": form,
    }
    return render(request, "login.html", context)

