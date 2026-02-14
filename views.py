from django.shortcuts import render , redirect
from email import message
from urllib import request
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .models import  Doctor , Patient , Appontment , Bill , Patient_login , Docter_login

# Create your views here.

def Admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = authenticate(request, username=username , password=password)
        
        if User is not None:
            login(request,User)
            return redirect('admin_crud')
        else:
            return redirect('login_admin')
    return render(request, 'Login_admin.html')

def Patients_SingUp(request):
    if request.method == "POST":
        try:
            Patient_login.objects.create(
                pname = request.POST.get('pname'),
                pemail_id = request.POST.get('pemail_id'),
                ppassword = request.POST.get('ppassword'),
            )
        
            return redirect('patient_login_crude')
        except:
            return redirect('Patient/Singup_patient')
    
    
    return render(request, 'Patient/SingUp_patient.html')

def Patients_login(request):
    if request.method == "POST":
        pemail_id = request.POST.get('pemail_id')
        ppassword = request.POST.get('ppassword')
        
        try:
            patient = Patient_login.objects.get(ppassword=ppassword,pemail_id=pemail_id)
            return redirect('patient_login_crude')
        except:
            return redirect('Login_Patient')
    return render(request,'Patient/Login_Patient.html')

def SingUp_Doceter(request):
    if request.method == "POST":
        try:
            Docter_login.objects.create(
                dname = request.POST.get('dname'),
                demail = request.POST.get('demail'),
                dpassword = request.POST.get('dpassword'),
            )
            return redirect('Docter_login_CRUD')
        except:
            return redirect('Singup_Docter')
    return render(request, 'Docter/SingUp_Docter.html')

def Login_Docter(request):
    if request.method == "POST":
        demail = request.POST.get('demail')
        dpassword = request.POST.get('dpassword')
        
        try:
            docter = Docter_login.objects.get(demail=demail,dpassword=dpassword)
            return redirect('Docter_login_CRUD')
        except :
            return redirect('Login_Docter')
    return render(request, 'Docter/Login_Docter.html')


def Add_Docter_details(request):
    if request.method == "POST" :
        Doctor.objects.create(
            did = request.POST.get('did'),
            dname = request.POST.get('dname'),
            demail = request.POST.get('demail'),
            dmob_no = request.POST.get('dmob_no'),
            speciality = request.POST.get('speciality'),
            experience = request.POST.get('experience'),
            dpassword  = request.POST.get('dpassword')
        )
        return HttpResponse('docter data add sucessfully')
    return render(request,'Docter/Add_Docter.html')

def Delate_Docter(request):
    if request.method == 'POST':
        did = request.POST.get('did')
        
        try:
            delate_doc = Doctor.objects.get(did=did)
            delate_doc.delete()
            return HttpResponse("docter is delated sucessfully !")
        
        except:
            return HttpResponse('docter is not found')
        
    return render(request, 'Docter/Delete_Docters.html')

def Show_all_Docters(request):
    Docters_data = Doctor.objects.all()
    return render(request,'Docter/View_Docter.html',{'Docters_data' : Docters_data}) 

def Update_Docter_Page(request):
    doc = ''
    
    if request.method == "POST":
        did = request.POST.get('dis')
        
        try:
            doc = Doctor.objects.get(did=did)
            doc.dname = request.POST.get('dname')
            doc.demail = request.POST.get('demail')
            doc.dmob_no = request.POST.get('dmob_no')
            doc.speciality = request.POST.get('speciality')
            doc.experience = request.POST.get('experience')
            dpassword  = request.POST.get('dpassword')
            doc.save()
            return HttpResponse("update sucessfully !")
        except:
            return HttpResponse("not update record")
        
    return render(request, 'Docter/Update_Docter.html' , {'doc' : doc})

def add_patient(request):
    if request.method == 'POST':
        Patient.objects.create(
            pid = request.POST.get('pid'),
            pname = request.POST.get('pname'),
            pemail = request.POST.get('pemail'),
            pmob_no = request.POST.get('pmob_no'),
            page = request.POST.get('page'),
            pgender = request.POST.get('pgender'),
            address = request.POST.get('address'),
        )
        
        return HttpResponse("add patient date !")
    return render(request, 'Patient/Add_Patient.html')

def Delate_Patient(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        
        try:
            pati = Patient.objects.get(pid=pid)
            pati.delete()
            return HttpResponse("data is deleted sucessfullay !")
        except:
            return HttpResponse("data is not delated !")
    return render(request, 'Patient/Delete_Patient.html')

def Show_Patient(request):
    patientss = Patient.objects.all()
    return render(request, 'Patient/View_Patient.html' , {'patientss' : patientss}) 

def Update_Patient(request):
    
    pati=''
    
    if request.method == "POST":
        pid = request.POST.get('pid') 
        
        try:
            pati = Patient.objects.get(pid=pid)
            pati.pname = request.POST.get('pname')
            pati.pemail = request.POST.get('pemail')
            pati.page = request.POST.get('page')
            pati.pgender = request.POST.get('pgender')
            pati.address = request.POST.get('address')
            pati.save()
            
            return HttpResponse("all is done")
        except :
            return HttpResponse('all is not done')
    return render(request,'Patient/Update_Patient.html')


def Add_Appointments(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        
        pid = request.POST.get('pid')
        patient_obj = Patient.objects.get(pk=pid)
        
        did = request.POST.get('did')
        doctor_obj = Doctor.objects.get(pk=did)
        
        
        if Appontment.objects.filter(date=date, time=time).exists():
            return HttpResponse('appintment is all ready book sellect another time')
        
        
        
        else:
            Appontment.objects.create(
                aid = request.POST.get('aid'),
                pid= patient_obj,
                did = doctor_obj,
                date = request.POST.get('date'),
                time = request.POST.get('time')
            )
            return HttpResponse('appint is add sucessfullys')
    return render(request, 'Appointment/Add_Appointment.html')

def Show_All_Appintmetn(request):
    apintment = Appontment.objects.all()
    return render(request, 'Appointment/View_Appintment.html', {'apintment':apintment})

def Delete_Appuntment(request):
    if request.method == 'POST':
        aid =request.POST.get('aid')
        try:
            dela = Appontment.objects.get(aid=aid)
            dela.delete()
            return HttpResponse("delete sucessfully")
        except:
            return HttpResponse('user not found')
    return render(request, 'Appointment/Delete_Appointment.html')

def Update_Appointments_status(request):
    uas = ''
    
    if request.method == "POST":
        aid = request.POST.get('aid')
        
        try:
            uas = Appontment.objects.get(aid=aid)
            uas.status = request.POST.get('status')
            uas.save()
            return HttpResponse("update dome")
        except :
            return HttpResponse("not done")
    return render(request , 'Docter/Update_Appointment_status.html')

def Update_appintment_detail(request):
    uad = ''
    if request.method == "POST":
        aid = request.POST.get('aid')
        date = request.POST.get('date')
        time = request.POST.get('time')
        
        pid = request.POST.get('pid')
        patient_obj = Patient.objects.get(pk=pid)
        
        did = request.POST.get('did')
        doctor_obj = Doctor.objects.get(pk=did)
        
        if Appontment.objects.filter(date=date, time=time).exists():
            return HttpResponse("appint is allready book")
        else:
            try:
                uad = Appontment.objects.get(aid=aid)
                uad.pid=patient_obj
                uad.did=doctor_obj
                uad.date=request.POST.get('date')
                uad.time=request.POST.get('time')
                uad.save()
            
                return HttpResponse('data is update done')
            except:
                return HttpResponse('appintment  is not found')
    return render(request, 'Appointment/Update_appintment_details.html')

def Add_Billing(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        patient_obj = Patient.objects.get(pk=pid)
        
        Bill.objects.create(
            bid = request.POST.get('bid'),
            pid = patient_obj,
            amount = request.POST.get('amount'),
            paid = request.POST.get('paid'),
            bill_date=request.POST.get('bill_date')
            
        )
        
        return HttpResponse('add is done')
    return render(request, 'Billing/Add_Bill.html')

def Delete_Bills(request):
    if request.method == "POST":
        bid = request.POST.get('bid')
        
        try:
            dela = Bill.objects.get(bid=bid)
            dela.delete()
            return HttpResponse("delate sucessfully !")
        except :
            return HttpResponse("not delete")
    return render(request,'Billing/Delete_Bill.html')

def show_all_bill_records(request):
    Bills = Bill.objects.all()
    return render(request, 'Billing/View_all_bills.html',{'Bills' : Bills})

def Update_Bills_Amount(request):
    dele = ''
    
    if request.method == "POST":
        bid = request.POST.get('bid')
        
        try:
            dele = Bill.objects.get(bid=bid)
            dele.amount = request.POST.get('amount')
            dele.save()
            return HttpResponse("update done")
        except:
            return HttpResponse("bill not found")
    return render(request, 'Billing/Update_Bill_Amount.html')

def Update_Bill_Status(request):
    delea = ''
    
    if request.method == "POST":
        bid = request.POST.get('bid')
        
        try:
            delea = Bill.objects.get(bid=bid)
            delea.paid = request.POST.get('paid')
            delea.save()
            return HttpResponse("all is done")
        except :
            return HttpResponse("not done")
    return render(request, 'Billing/Update_Bill_Status.html')

def patient_crud(request):
    return render(request, 'Patient/Patient_CRUD.html')

def docter_crud(request):
    return render(request, 'Docter/Docter_CRUD.html')

def bill_crud(request):
    return render(request, 'Billing/Billin_CRUD.html')

def appintment_crud(request):
    return render(request, 'Appointment/Appintment_CRUD.html')

def admin_crud(request):
    return render(request, 'Admin_page.html')

def Docter_login_CRUD(request):
    return render(request, 'Docter/Docter_login_CRUD.html')

from django.shortcuts import render
from .models import Patient

def view_patient_profile(request):
    patient = Patient.objects.get(user=request.user)
    return render(request, 'Patient/view_profile.html', {'patient': patient})

def patient_login(request):
    return render(request, 'Patient/Patient_Login_CRUD.html')

