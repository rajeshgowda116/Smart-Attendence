from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import Registrationform


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






