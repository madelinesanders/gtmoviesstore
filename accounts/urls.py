from django.urls import path
from django.contrib.auth import views as auth_views  # Import auth views for password change
from . import views

urlpatterns = [
    path('signup/', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),

    # Password Change Feature
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html',
        success_url='/accounts/change-password/done/'
    ), name='accounts.change_password'),

    path('change-password/done/', views.password_change_done, name='accounts.password_change_done'),
]
