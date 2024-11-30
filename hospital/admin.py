from django.contrib import admin
from .models import Patient

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'gender', 'phone_number', 'membership_number')
    list_filter = ('gender', 'status', 'created_at')
    search_fields = ('full_name', 'id_number', 'phone_number', 'email')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'date_of_birth', 'gender', 'address', 'phone_number', 
                      'email', 'id_number', 'status', 'occupation', 'are_you_retired')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_relationship', 'emergency_contact_phone')
        }),
        ('Office Use Only', {
            'fields': ('membership_number', 'membership_type', 'payment_type', 'staff_name', 'staff_signature')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
