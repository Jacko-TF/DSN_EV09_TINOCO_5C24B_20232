from django.urls import path
from .import views

app_name = 'myapp'

urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('login',views.login_form),
    path('logueo',views.logueo),
    path('logout',views.logout),
    path('registro',views.registro),
    path('register',views.register),
]