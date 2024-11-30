from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import Patient
from .forms import PatientForm, PatientSearchForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

def home(request):
    return render(request, 'hospital/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'تم إنشاء الحساب بنجاح!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'hospital/signup.html', {'form': form})

@login_required
def dashboard(request):
    patients_count = Patient.objects.count()
    recent_patients = Patient.objects.order_by('-created_at')[:5]
    context = {
        'patients_count': patients_count,
        'recent_patients': recent_patients,
    }
    return render(request, 'hospital/dashboard.html', context)

@login_required
def profile(request):
    return render(request, 'hospital/profile.html')

@login_required
def patient_list(request):
    search_form = PatientSearchForm(request.GET)
    patients = Patient.objects.all().order_by('-id')

    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        if search_query:
            patients = patients.filter(
                Q(full_name__icontains=search_query) |
                Q(id_number__icontains=search_query)
            )

    context = {
        'title': 'قائمة المرضى',
        'patients': patients,
        'search_form': search_form
    }
    return render(request, 'hospital/patient_list.html', context)

@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            messages.success(request, 'تمت إضافة المريض بنجاح!')
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'hospital/add_patient.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'hospital/patient_list.html'
    context_object_name = 'patients'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'قائمة المرضى'
        return context

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = 'hospital/patient_form.html'
    fields = [
        'full_name', 'date_of_birth', 'gender', 'address', 'phone_number',
        'email', 'id_number', 'status', 'occupation', 'are_you_retired',
        'emergency_contact_name', 'emergency_contact_relationship', 'emergency_contact_phone',
        'membership_number', 'membership_type', 'payment_type', 'staff_name', 'staff_signature'
    ]
    success_url = reverse_lazy('patient_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'إضافة مريض جديد'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'تم إضافة المريض بنجاح!')
        return super().form_valid(form)

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'hospital/edit_patient.html'
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        messages.success(self.request, 'تم تحديث بيانات المريض بنجاح.')
        return super().form_valid(form)

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'hospital/delete_patient.html'
    success_url = reverse_lazy('patient_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'تم حذف المريض بنجاح.')
        return super().delete(request, *args, **kwargs)
