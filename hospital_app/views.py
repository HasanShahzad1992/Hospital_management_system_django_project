from django.shortcuts import render,redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from hospital_app import models


def load_hospital_add_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username = initial_request_from_front_end.session["username"]
        return render(initial_request_from_front_end,"load_hospital_add_user.html",{"username":username})
def add_hospital_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        name_of_hospital=initial_request_from_front_end.POST.get("name_hospital")
        models.Hospital.objects.create(hospital_name=name_of_hospital)
        return render(initial_request_from_front_end,"load_hospital_add_user.html",{"message":"hospital successfully added","username":username})
def view_all_hospitals_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_hospitals_objects=models.Hospital.objects.all()
        return render(initial_request_from_front_end,"view_all_hospitals.html",{"all_hospitals":all_hospitals_objects,"username":username})
def load_hospital_update_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_hospitals_objects = models.Hospital.objects.all()
        return render(initial_request_from_front_end,"load_update_hospital.html",{"all_hospitals":all_hospitals_objects,"username":username})
def update_hospital_html(initial_request_from_front_end,updated_hospital_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_hospitals_objects = models.Hospital.objects.all()
        updated_hospital_name=initial_request_from_front_end.POST.get("name_hospital")
        particular_updated_hospital_object=models.Hospital.objects.get(hospital_id=updated_hospital_id)
        particular_updated_hospital_object.hospital_name=updated_hospital_name
        particular_updated_hospital_object.save()
        return render(initial_request_from_front_end,"load_update_hospital.html",{"all_hospitals":all_hospitals_objects,"message":"successfully updated","username":username})
def load_hospital_delete_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username = initial_request_from_front_end.session["username"]
        all_hospitals_objects = models.Hospital.objects.all()
        return render(initial_request_from_front_end,"load_delete_hospital.html",{"all_hospitals":all_hospitals_objects,"username":username})
def delete_hospital_html(initial_request_from_front_end,deleted_hospital_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_hospitals_objects = models.Hospital.objects.all()
        particular_hospital_object=models.Hospital.objects.get(hospital_id=deleted_hospital_id)
        particular_hospital_object.delete()
        return render(initial_request_from_front_end,"load_delete_hospital.html",{"all_hospitals":all_hospitals_objects,"message":"hospital_successfully_deleted","username":username})
def load_doctor_add_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        return render(initial_request_from_front_end,"load_add_doctor.html",{"username":username})
def add_doctor_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        name_of_new_doctor=initial_request_from_front_end.POST.get("name_doctor")
        name_of_specialization_new_doctor=initial_request_from_front_end.POST.get("specialization_doctor")
        models.Doctor.objects.create(doctor_name=name_of_new_doctor,doctor_specialization=name_of_specialization_new_doctor)
        return render(initial_request_from_front_end,"load_add_doctor.html",{"message":"new_doctor_successfully_added","username":username})
def view_all_doctor_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_doctor_objects=models.Doctor.objects.all()
        return render(initial_request_from_front_end,"view_all_doctors.html",{"all_doctors":all_doctor_objects,"username":username})
def load_doctor_update_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_doctor_objects=models.Doctor.objects.all()
        return render(initial_request_from_front_end,"load_update_doctor.html",{"all_doctors":all_doctor_objects,"username":username})
def update_doctor_html(initial_request_from_front_end,updated_doctor_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_doctor_objects = models.Doctor.objects.all()
        updated_doctor_name=initial_request_from_front_end.POST.get("new_doctor_name")
        updated_doctor_specialization=initial_request_from_front_end.POST.get("new_doctor_specialization")
        particular_doctor_object=models.Doctor.objects.get(doctor_id=updated_doctor_id)
        particular_doctor_object.doctor_name=updated_doctor_name
        particular_doctor_object.doctor_specialization=updated_doctor_specialization
        particular_doctor_object.save()
        return render(initial_request_from_front_end,"load_update_doctor.html",{"all_doctors":all_doctor_objects,"message":"doctor_details_updated_successfully","username":username})
def load_doctor_html_delete(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_doctor_objects=models.Doctor.objects.all()
        return render(initial_request_from_front_end,"load_delete_doctor.html",{"all_doctor":all_doctor_objects,"username":username})
def delete_doctor_html(initial_request_from_front_end,delete_doctor_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_doctor_objects = models.Doctor.objects.all()
        particular_doctor_object=models.Doctor.objects.get(doctor_id=delete_doctor_id)
        particular_doctor_object.delete()
        return render(initial_request_from_front_end,"load_delete_doctor.html",{"all_doctor":all_doctor_objects,"message":"doctor_successfully_deleted","username":username})
def load_hospital_doctor_combined_add_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username = initial_request_from_front_end.session["username"]
        all_hospital_objects=models.Hospital.objects.all()
        all_doctor_objects=models.Doctor.objects.all()
        return render(initial_request_from_front_end,"load_add_hospital_doctor_combined.html",{"all_hospitals":all_hospital_objects,"all_doctors":all_doctor_objects,"username":username})
def add_hospital_doctor_combined(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_hospital_objects = models.Hospital.objects.all()
        all_doctor_objects = models.Doctor.objects.all()
        id_of_added_hospital=initial_request_from_front_end.POST.get("id_of_added_hospital")
        id_of_added_doctor=initial_request_from_front_end.POST.get("id_of_added_doctor")
        days_a_doctor_active=initial_request_from_front_end.POST.get("days that a doctor is active in a hospital")
        models.Hospital_Doctor.objects.create(hospital_id=id_of_added_hospital,doctor_id=id_of_added_doctor,days_active= days_a_doctor_active)
        return render(initial_request_from_front_end,"load_add_hospital_doctor_combined.html",{"all_hospitals":all_hospital_objects,"all_doctors":all_doctor_objects,"message":"hospital_doctor_combined_successfully_added","username":username})
def view_all_hospital_doctor_combined(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_hospital_doctor_combined_objects=models.Hospital_Doctor.objects.all()
        return render(initial_request_from_front_end,"view_all_hospital_doctor_combined.html",{"all_hospital_doctor_combined":all_hospital_doctor_combined_objects,"username":username})
def load_hospital_doctor_combined_update_html(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        all_hospital_doctor_combined_objects = models.Hospital_Doctor.objects.all()
        all_hospitals_objects=models.Hospital.objects.all()
        all_doctor_objects=models.Doctor.objects.all()
        return render(initial_request_from_front_end,"load_update_hospital_doctor_combined.html",{"all_hospital_doctor_combined":all_hospital_doctor_combined_objects,"all_hospital":all_hospitals_objects,"all_doctor":all_doctor_objects,"username":username})
def update_hospital_doctor_html(initial_request_from_front_end,updated_hospital_doctor_combined_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        all_hospital_doctor_combined_objects=models.Hospital_Doctor.objects.all()
        all_hospitals_objects=models.Hospital.objects.all()
        all_doctor_objects=models.Doctor.objects.all()
        updated_hospital_id=initial_request_from_front_end.POST.get("hospital_id_to_be_updated")
        updated_doctor_id=initial_request_from_front_end.POST.get("doctor_id_to_be_updated")
        updated_days_active=initial_request_from_front_end.POST.get("updated_days_of_activity_for_a_doctor")
        particular_hospital_doctor_combined_object=models.Hospital_Doctor.objects.get(hospital_doctor_id=updated_hospital_doctor_combined_id)
        particular_hospital_doctor_combined_object.hospital_id=updated_hospital_id
        particular_hospital_doctor_combined_object.doctor_id=updated_doctor_id
        particular_hospital_doctor_combined_object.days_active=updated_days_active
        particular_hospital_doctor_combined_object.save()
        return render(initial_request_from_front_end,"load_update_hospital_doctor_combined.html",{"all_hospital_doctor_combined":all_hospital_doctor_combined_objects,"all_hospital":all_hospitals_objects,"all_doctor":all_doctor_objects,"message":"updated_successfully","username":username})

def load_hospital_doctor_combined_delete(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        username=initial_request_from_front_end.session["username"]
        hospital_doctor_combined_objects=models.Hospital_Doctor.objects.all()
        return render(initial_request_from_front_end,"load_delete_hospital_doctor_combined.html",{"hospital_doctor_combined_objects":hospital_doctor_combined_objects,"username":username})
def delete_hospital_doctor_combined(initial_request_from_front_end,delete_hospital_doctor_combined_id):
    if initial_request_from_front_end.method=="POST":
        username=initial_request_from_front_end.session["username"]
        hospital_doctor_combined_objects = models.Hospital_Doctor.objects.all()
        particular_hospital_doctor_combined_object=models.Hospital_Doctor.objects.get(hospital_doctor_id=delete_hospital_doctor_combined_id)
        particular_hospital_doctor_combined_object.delete()
        return render(initial_request_from_front_end,"load_delete_hospital_doctor_combined.html",{"hospital_doctor_combined_objects":hospital_doctor_combined_objects,"message":"successfully deleted","username":username})

def load_medical_system_signup(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        return render(initial_request_from_front_end,"load_signup_medical_system.html")

def signup_medical_system(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        chosen_username=initial_request_from_front_end.POST.get("username_to_be_chosen")
        chosen_email=initial_request_from_front_end.POST.get("email_to_be_chosen")
        chosen_password=initial_request_from_front_end.POST.get("password_to_be_chosen")
        particular_signup_object=models.Medical_System_Users.objects.create(medical_system_user_name=chosen_username,medical_system_email=chosen_email,medical_system_password=chosen_password,medical_system_user_type="entry")
        return render(initial_request_from_front_end,"load_signup_medical_system.html",{"message":"sign_up_successful"})

def load_medical_system_login(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            username=initial_request_from_front_end.session["username"]
            return redirect("load_medical_system_home_page")
        except:
            return render(initial_request_from_front_end, "load_login_medical_system.html")
def login_medical_system(initial_request_from_front_end):
    if initial_request_from_front_end.method=="POST":
        email_user=initial_request_from_front_end.POST.get("email_typed")
        password_user=initial_request_from_front_end.POST.get("password_typed")
        print(email_user,"EM")
        print(password_user,"Pw")
        try:
            particular_medical_system_object=models.Medical_System_Users.objects.get(medical_system_email=email_user,medical_system_password=password_user)
            print("hello")
            initial_request_from_front_end.session["username"]=particular_medical_system_object.medical_system_user_name
            initial_request_from_front_end.session["usertype"]=particular_medical_system_object.medical_system_user_type
            initial_request_from_front_end.session["userid"]=particular_medical_system_object.medical_syster_user_id
            if initial_request_from_front_end.session["usertype"]=="admin":
                return redirect("load_admin_medical_system_home_page")
            elif initial_request_from_front_end.session["usertype"]=="entry":
                return redirect("load_entry_medical_system_home_page")
        except:
            return render(initial_request_from_front_end, "load_login_medical_system.html", {"message": "wrong_password or email"})
def load_admin_medical_system_home_page(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            username=initial_request_from_front_end.session["username"]
            usertype=initial_request_from_front_end.session["usertype"]
            userid=initial_request_from_front_end.session["userid"]
            if usertype=="admin":
                return render(initial_request_from_front_end, "load_admin_home_medical_system.html", {"username":username,"userid":userid})
            elif usertype=="entry":
                return redirect("load_entry_medical_system_home_page")
        except:
            return redirect("load_medical_system_login")
def load_entry_medical_system_home_page(initial_request_from_front_end):
    if initial_request_from_front_end.method=="GET":
        try:
            username=initial_request_from_front_end.session["username"]
            usertype=initial_request_from_front_end.session["usertype"]
            userid=initial_request_from_front_end.session["userid"]
            if usertype=="entry":
                return render(initial_request_from_front_end,"load_entry_home_medical_system.html",{"username":username,"userid":userid})
            elif usertype=="admin":
                return redirect("load_admin_medical_system_home_page")
        except:
            return redirect("load_medical_system_login")
def logout_medical_system(initial_request_from_front_end):
    initial_request_from_front_end.session.flush()
    return redirect("load_medical_system_login")

def upload_picture(initial_request_from_front_end,userid):
    if initial_request_from_front_end.method=="POST":
            profile_picture_uploaded_server=initial_request_from_front_end.FILES.get("profile_picture")
            particular_picture_object=models.Medical_System_Users.objects.get(medical_syster_user_id=userid)
            particular_picture_object.upload_profile_picture=profile_picture_uploaded_server
            particular_picture_object.save()
            if initial_request_from_front_end.session["usertype"]=="admin":
                return redirect("load_admin_medical_system_home_page")
            elif initial_request_from_front_end.session["usertype"]=="entry":
                return redirect("load_entry_medical_system_home_page")