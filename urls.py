"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.Admin_login , name='login_admin'),
    path('SingUp_Patient/',views.Patients_SingUp , name='Singup_patient'),
    path('Login_Patient/' , views.Patients_login , name='Login_Patient'),
    path('SingUp_Docter/' , views.SingUp_Doceter , name='Singup_Docter'),
    path('Login_Docter/' , views.Login_Docter , name='Login_Docter'),
    path('Add_Docter/' , views.Add_Docter_details , name='Add_Docter'),
    path('Delete_docters/' , views.Delate_Docter , name='Delete_Docter'),
    path('Show_All_Docters/' , views.Show_all_Docters, name="show_all_docter"),
    path('Update_Docter_Record/' , views.Update_Docter_Page, name='Update_docter_record'),
    path('Add_Patient/' , views.add_patient , name='add_patient'),
    path('Delete_Patient/', views.Delate_Patient , name='Delete_pationts'),
    path('Show_All_Patients/', views.Show_Patient , name='show_all_patient'),
    path('Update_Patient/',views.Update_Patient , name='Update_patinet'),
    path('Add_Appointment/',views.Add_Appointments, name='Add_Appointments'),
    path('Show_Appintment/',views.Show_All_Appintmetn,name='Show_all_appintment'),
    path('Delete_Appintment/' , views.Delete_Appuntment , name='Delete_appointment'),
    path('Update_Appointment_statu/' , views.Update_Appointments_status , name='Update_Appointment_status'),
    path('Update_appintment_detail/' , views.Update_appintment_detail , name='Update_appintment_details'),
    path('Add_Bill/' , views.Add_Billing , name='Add_bills'),
    path('Delete_Bills/' , views.Delete_Bills , name='Delete_bill'),
    path("Show_All_Bills/" , views.show_all_bill_records , name="showe_All_bills"),
    path('Update_Bill Amount/' , views.Update_Bills_Amount , name="update_bill_amount"),
    path('Update_Bill_Paid/' , views.Update_Bill_Status , name="update_bill_opaid_or_not"),
    path('patient_crud/' , views.patient_crud , name="patient_crud"),
    path('docter_crud/' , views.docter_crud , name='docter_crud'),
    path('bill_crud/' , views.bill_crud , name='billing_crud'),
    path('appointment_crud/' , views.appintment_crud , name="appintntment_crud"),
    path('admin_crud/' , views.admin_crud , name="admin_crud"),
    path('Docter_login_CRUD/' , views.Docter_login_CRUD , name="Docter_login_CRUD"),
    path('profile/', views.view_patient_profile, name='view_patient_profile'),
    path('patient_loogin_crud/', views.patient_login, name='patient_login_crude'),
    
]
