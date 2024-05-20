from django.urls import path
from . import views

urlpatterns = [
path('main/', views.main, name='main'),
path('register/', views.registerUser, name='register'),
path('registerdUsers/', views.registerdUsers, name='registerdUsers'),
path('registerdUsers/deleteUser/<int:id>/', views.deleteUser, name='deleteUser'),  
path('registerdUsers/editUser/<int:id>/', views.editUser, name='editUser'),
]