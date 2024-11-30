from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'ذكر'),
        ('F', 'أنثى'),
    ]
    
    STATUS_CHOICES = [
        ('single', 'أعزب'),
        ('married', 'متزوج'),
        ('divorced', 'مطلق'),
        ('widowed', 'أرمل'),
        ('other', 'آخر'),
    ]

    # Personal Information - المعلومات الشخصية
    full_name = models.CharField(max_length=100, verbose_name='الاسم الكامل', default='')
    date_of_birth = models.DateField(verbose_name='تاريخ الميلاد', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='الجنس', default='M')
    address = models.TextField(verbose_name='العنوان', default='')
    phone_number = models.CharField(max_length=20, verbose_name='رقم الهاتف', default='')
    email = models.EmailField(verbose_name='البريد الإلكتروني', blank=True, null=True)
    id_number = models.CharField(max_length=50, verbose_name='رقم الهوية', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='الحالة الاجتماعية', blank=True)
    occupation = models.CharField(max_length=100, verbose_name='المهنة', blank=True)
    are_you_retired = models.BooleanField(verbose_name='هل أنت متقاعد؟', default=False)

    # Emergency Contact Details - معلومات الاتصال في حالات الطوارئ
    emergency_contact_name = models.CharField(max_length=100, verbose_name='اسم شخص للاتصال به في حالات الطوارئ', blank=True)
    emergency_contact_relationship = models.CharField(max_length=50, verbose_name='صلة القرابة', blank=True)
    emergency_contact_phone = models.CharField(max_length=20, verbose_name='رقم هاتف الطوارئ', blank=True)

    # Office Use Only - لاستخدام المكتب فقط
    membership_number = models.CharField(max_length=50, verbose_name='رقم العضوية', blank=True)
    membership_type = models.CharField(max_length=50, verbose_name='نوع العضوية', blank=True)
    payment_type = models.CharField(max_length=50, verbose_name='طريقة الدفع', blank=True)
    staff_name = models.CharField(max_length=100, verbose_name='اسم الموظف', blank=True)
    staff_signature = models.CharField(max_length=100, verbose_name='توقيع الموظف', blank=True)

    # Medical Information
    diagnosis = models.TextField(verbose_name='التشخيص', blank=True)
    medical_history = models.TextField(verbose_name='التاريخ الطبي', blank=True)
    current_medications = models.TextField(verbose_name='الأدوية الحالية', blank=True)
    allergies = models.TextField(verbose_name='الحساسية', blank=True)
    blood_type = models.CharField(
        max_length=5,
        verbose_name='فصيلة الدم',
        choices=[
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
        ],
        blank=True
    )

    # Document uploads
    medical_reports = models.FileField(
        upload_to='medical_reports/%Y/%m/',
        verbose_name='التقارير الطبية',
        blank=True,
        help_text='يمكنك تحميل ملفات PDF أو صور للتقارير الطبية'
    )
    lab_results = models.FileField(
        upload_to='lab_results/%Y/%m/',
        verbose_name='نتائج التحاليل',
        blank=True,
        help_text='يمكنك تحميل ملفات PDF أو صور لنتائج التحاليل'
    )
    prescriptions = models.FileField(
        upload_to='prescriptions/%Y/%m/',
        verbose_name='الوصفات الطبية',
        blank=True,
        help_text='يمكنك تحميل ملفات PDF أو صور للوصفات الطبية'
    )

    # System Fields - حقول النظام
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')
    
    class Meta:
        verbose_name = 'مريض'
        verbose_name_plural = 'المرضى'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.full_name
