from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomErrorList, CustomLoginForm

User = get_user_model()


@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')


def login(request):
    template_data = {'title': 'Login'}

    if request.method == 'GET':
        template_data['form'] = CustomLoginForm()
        return render(request, 'accounts/login.html', {'template_data': template_data})

    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
                user = authenticate(username=user.username, password=password)

                if user:
                    auth_login(request, user)
                    return redirect('home')
            except User.DoesNotExist:
                form.add_error(None, "Invalid email or password.")

        template_data['form'] = form
        return render(request, 'accounts/login.html', {'template_data': template_data})


def signup(request):
    template_data = {'title': 'Sign Up'}

    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data': template_data})

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')

        template_data['form'] = form
        return render(request, 'accounts/signup.html', {'template_data': template_data})


@login_required
def orders(request):
    template_data = {'title': 'Orders', 'orders': request.user.order_set.all()}
    return render(request, 'accounts/orders.html', {'template_data': template_data})
