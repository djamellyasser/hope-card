from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'full_name', 'date_of_birth', 'gender', 'phone_number',
            'email', 'address', 'id_number', 'status', 'occupation',
            'are_you_retired', 'emergency_contact_name',
            'emergency_contact_relationship', 'emergency_contact_phone',
            'membership_number', 'membership_type', 'payment_type',
            'staff_name', 'staff_signature',
            # Medical Information
            'diagnosis', 'medical_history', 'current_medications',
            'allergies', 'blood_type',
            # Document uploads
            'medical_reports', 'lab_results', 'prescriptions'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 2}),
            'diagnosis': forms.Textarea(attrs={'rows': 3}),
            'medical_history': forms.Textarea(attrs={'rows': 3}),
            'current_medications': forms.Textarea(attrs={'rows': 3}),
            'allergies': forms.Textarea(attrs={'rows': 2}),
        }
        labels = {
            'full_name': 'الاسم الكامل',
            'date_of_birth': 'تاريخ الميلاد',
            'gender': 'الجنس',
            'address': 'العنوان',
            'phone_number': 'رقم الهاتف',
            'email': 'البريد الإلكتروني',
            'id_number': 'رقم الهوية',
            'status': 'الحالة الاجتماعية',
            'occupation': 'المهنة',
            'are_you_retired': 'هل أنت متقاعد؟',
            'emergency_contact_name': 'اسم شخص للاتصال به في حالات الطوارئ',
            'emergency_contact_relationship': 'صلة القرابة',
            'emergency_contact_phone': 'رقم هاتف الطوارئ'
        }

class PatientSearchForm(forms.Form):
    search_query = forms.CharField(
        label='بحث بالاسم أو رقم الهوية',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ادخل الاسم أو رقم الهوية...'
        })
    )
