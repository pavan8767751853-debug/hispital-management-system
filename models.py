from django.db import models

# Create your models here.

class Patient(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=100)
    pemail = models.EmailField(max_length=200)
    pmob_no = models.BigIntegerField()
    page = models.IntegerField()
    pgender = models.CharField(max_length=100)
    address = models.TextField(max_length=3000)
    
    def __str__(self):
        return self.pname
    
class Doctor(models.Model):
    did = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=100)
    demail = models.EmailField()
    dmob_no = models.BigIntegerField()
    speciality = models.CharField(max_length=200)
    experience = models.IntegerField()
    
    def __str__(self):
        return self.dname
    
class Appontment(models.Model):
    aid = models.IntegerField(primary_key=True)
    pid = models.ForeignKey(Patient, on_delete=models.CASCADE)
    did = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=1000)
    
    def __str__(self):
        return f"{self.patient} - {self.doctor}"
    
class Bill(models.Model):
    bid = models.IntegerField(primary_key=True)
    pid = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    paid = models.CharField()
    bill_date = models.DateField()
    
    def __str__(self):
        return f"Bill {self.bid} - {self.patient}"
    
class Patient_login(models.Model):
    pname = models.CharField(max_length=200)
    pemail_id = models.EmailField(primary_key=True)
    ppassword = models.BigIntegerField()
    
    def __str__(self):
        return self.pemail_id
    
class Docter_login(models.Model):
    dname= models.CharField(max_length=200)
    demail = models.EmailField()
    dpassword = models.IntegerField()
    
    def __str__(self):
        return self.dname
    
    
