from django.contrib import admin
from .models import User    # Import your User model

# Register the User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['first_name', 'last_name']