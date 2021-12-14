from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}! You are now able to log in')
      form.save() # takes care of creating the user, hashing the password, etc.
      return redirect('/login/')
  else:
    form = UserRegisterForm()

  context = {
    'form': form
  }
  return render(request, 'users/register.html', context)


def login(request):
  pass


@login_required
def profile(request):
  return render(request, 'users/profile.html')

