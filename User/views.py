
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .forms import  Registrationform



def register(request):
    if request.method == "POST":
        form = Registrationform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please sign in with your new account.")
            return redirect("login")
    else:
        form = Registrationform()

    return render(request, "register.html", {"form": form})


def login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
        messages.error(request, "Invalid username or password.")
    return render(request, "login.html", {"form": form})


