from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register_page'),
    path('login/', views.user_login, name='login_page'),
    path('logout/', views.user_logout, name='logout')
]
