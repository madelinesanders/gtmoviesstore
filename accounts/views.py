from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomErrorList

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')  # Ensure 'home' is the correct URL name

def login(request):
    template_data = {'title': 'Login'}

    if request.method == 'GET':
        return render(request, 'accounts/login.html', template_data)

    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))

        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html', template_data)

        auth_login(request, user)
        return redirect('home')

def signup(request):
    template_data = {'title': 'Sign Up'}

    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', template_data)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')  # Redirects to login after signup

        template_data['form'] = form
        return render(request, 'accounts/signup.html', template_data)
