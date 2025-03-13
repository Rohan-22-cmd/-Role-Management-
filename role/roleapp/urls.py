from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_dashboard, name='role_dashboard'),  # Dashboard view
    path('create/', views.create_role, name='create_role'),  # Create role view
    path('update/<int:role_id>/', views.update_role, name='update_role'),  # Update role view
    path('role/delete/<int:role_id>/', views.delete_role, name='delete_role')
    ]

