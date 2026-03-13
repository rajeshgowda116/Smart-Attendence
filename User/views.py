from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import Registrationform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.http import HttpResponse



def register(request):
  if request.method == 'POST':
    form = Registrationform(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Registration successful. Your account is now in the admin user list.')
      return redirect('register')
  else:
    form = Registrationform()

  return render(request, 'register.html', {'form': form})

def login(request):
  if request.method == 'POST':
    form=AuthenticationForm(request,data=request.POST)
    if form.is_valid():
      username=form.cleaned_data.get('username')
      password=form.cleaned_data.get('password')
      user=auth.authenticate(username=username,password=password)
      if user is not None:
        auth.login(request,user)
        return HttpResponse(f"<h1>Hii bevarsi {username}<h1> ")
      
    else:
      form=AuthenticationForm()
  return render(request,"login.html")





