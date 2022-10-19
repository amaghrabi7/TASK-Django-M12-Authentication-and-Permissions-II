from pdb import post_mortem
from django.shortcuts import render, redirect
from users.forms import UserRegister
from django.contrib.auth import login, logout

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
    return redirect("register")
