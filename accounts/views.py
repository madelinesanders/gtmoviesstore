from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomErrorList

@login_required
def logout(request):
    auth_logout(request)
    return redirect('landing.index')  # Ensure 'home' is correctly named in urls.py

def login(request):
    template_data = {'title': 'Login'}

    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'template_data': template_data})

    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))

        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html', {'template_data': template_data})

        auth_login(request, user)
        return redirect('home')

def signup(request):
    template_data = {'title': 'Sign Up'}

    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data': template_data})

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')  # ✅ Fix: Redirect to correct login URL

        template_data['form'] = form
        return render(request, 'accounts/signup.html', {'template_data': template_data})
@login_required
def orders(request):
    template_data={}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html', {'template_data': template_data})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keeps the user logged in after password change
            return redirect('accounts.password_change_done')  # Redirect to confirmation page
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'accounts/password_change.html', {'form': form})

@login_required
def password_change_done(request):
    return render(request, 'accounts/password_change_done.html')