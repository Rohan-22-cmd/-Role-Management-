# roles/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Role
from .forms import RoleForm
from django.contrib.auth.decorators import login_required
# Admin-only check
def is_admin(user):
    return user.is_superuser

# Dashboard View (List all roles)
def role_dashboard(request):
    roles = Role.objects.all()  # Get all roles
    return render(request, 'roles/role_dashboard.html', {'roles': roles})
# Create Role View
@user_passes_test(is_admin)
def create_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_dashboard')
    else:
        form = RoleForm()
    return render(request, 'roles/create_role.html', {'form': form})

# Update Role View
@user_passes_test(is_admin)
def update_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_dashboard')
    else:
        form = RoleForm(instance=role)
    return render(request, 'roles/update_role.html', {'form': form, 'role': role})

# Soft Delete Role View



@login_required
def delete_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    
    if request.method == 'POST':
        role.delete()
        return redirect('role_dashboard')
    
    return render(request, 'roles/confirm_delete_role.html', {'role': role})
