from django.urls import path

from common import views

app_name = "common"

urlpatterns = [
    path('login/', views.common_login, name='login'),
    path('logout/', views.common_logout, name='logout'),
    path('profile/', views.common_profile, name='profile'),
    path('password/', views.common_password, name='password'),
]