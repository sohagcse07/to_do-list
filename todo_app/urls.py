from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
   
   path( '' , views.task_list , name='task_list'),
   path ( 'add/' , views.task_create , name='task_create' ),
   path ( 'edit/<int:pk>/' , views.task_update , name='task_update' ),
   path ( 'delete/<int:pk>/' , views.task_delete , name= 'task_delete' ),
   path('toggle/<int:pk>/', views.task_toggle, name='task_toggle'),

    # auth
   # path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
   # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
