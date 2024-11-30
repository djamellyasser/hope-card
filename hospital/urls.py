from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('patient/list/', views.patient_list, name='patient_list'),
    path('patient/add/', views.add_patient, name='add_patient'),
    path('patient/<int:pk>/edit/', views.PatientUpdateView.as_view(), name='edit_patient'),
    path('patient/<int:pk>/delete/', views.PatientDeleteView.as_view(), name='delete_patient'),
    path('login/', auth_views.LoginView.as_view(template_name='hospital/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
