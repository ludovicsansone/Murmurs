from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginView, name = 'authentication_login'),
    path('register/', views.registerView, name = 'authentication_register'),
    path('forget/', views.forgetView, name = 'authentication_forget'),
    path('logout/', views.logoutView, name = 'authentication_logout')
]
