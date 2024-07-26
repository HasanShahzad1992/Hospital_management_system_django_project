from django.db import models

class Hospital(models.Model):
    hospital_id=models.AutoField(primary_key=True)
    hospital_name=models.CharField(max_length=30)
class Doctor(models.Model):
    doctor_id=models.AutoField(primary_key=True)
    doctor_name=models.CharField(max_length=100)
    doctor_specialization=models.CharField(max_length=30)
class Hospital_Doctor(models.Model):
    hospital_doctor_id=models.AutoField(primary_key=True)
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    days_active=models.IntegerField()
class Medical_System_Users(models.Model):
    medical_syster_user_id=models.AutoField(primary_key=True)
    medical_system_user_name=models.CharField(max_length=30)
    medical_system_email=models.EmailField(unique=True)
    medical_system_password=models.CharField(max_length=30)
    medical_system_user_type=models.CharField(max_length=30)
    upload_profile_picture=models.ImageField(upload_to="profile_picture_hospital_user",default=True)
