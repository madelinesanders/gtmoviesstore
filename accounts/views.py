from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth.models import User

@login_required
def orders(request):
    template_data = {
        'title': 'Orders',
        'orders': request.user.order_set.all()
    }
    return render(request, 'accounts/orders.html', template_data)

def logout(request):
    auth_logout(request)
    return redirect('home.index')

def login(request):
    template_data = {'title': 'Login'}

    if request.method == 'GET':
        return render(request, 'accounts/login.html', template_data)

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html', template_data)
        else:
            auth_login(request, user)
            return redirect('home.index')  # Fixed redirect target

def signup(request):
    template_data = {'title': 'Sign Up'}

    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', template_data)

    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)  # Fixed misplaced parenthesis

        if form.is_valid():
            form.save()
            return redirect('home.index')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', template_data)
