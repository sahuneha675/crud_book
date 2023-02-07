from django.shortcuts import redirect, render
from django.contrib import messages
from django.http.response import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from datetime import date


from .models import *


# Create your views here.

def index(request):
    return render(request,"index.html")

def student_registration(request):
    return render(request, "registration.html")

def register_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll_no = request.POST['roll_no']
        dob = request.POST['birthdayDate']
        gender = request.POST['gender']
        email = request.POST['emailAddress']
        phone = request.POST['phone']
        subject = request.POST['subject']
        image = request.FILES['profile_image']
        password = make_password(request.POST['password'])
        
        if Student.objects.filter(email=email).exists():
            messages.error(request,"Email alrady exists")
            return redirect('/student_registration/')
        elif Student.objects.filter(phone=phone).exists():
            messages.error(request,"phone alrady exists")
            return redirect('/student_registration/')   
        else:
            Student.objects.create(name=name, roll_no=roll_no,
                                   email=email, gender=gender, 
                                   phone=phone, dob=dob, image=image,
                                   subject=subject, password=password)
            alert = True
            return render(request, "registration.html", {'alert':alert})

def student_login(request):
    return render(request,'student_login.html')

def login_form(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        user_password = request.POST['password']
        if Student.objects.filter(email=user_email).exists():
            obj = Student.objects.get(email=user_email)
            password = obj.password
            if check_password(user_password, password):
                d=Student.objects.filter(email=user_email)
                return render(request,'profile.html',{'d':d})
            else:
                messages.error(request,"password incorrect")
                alert = True
                return render(request,"student_login.html", {'alert':alert})
               #return HttpResponse('password incorrect')
        else:
            messages.error(request,"email is not registered")
            alert = True
            return render(request,"student_login.html", {'alert':alert})

            #return HttpResponse("email is not registered")

#@login_required(login_url = '/student_login')
def profile(request):
    return render(request, "profile.html")

def view_issued_book(request):
    issuedBooks = IssuedBook.objects.all()
    details = []
    for i in issuedBooks:
        days = (date.today()-i.issued_date)
        d=days.days
        fine=0
        if d>14:
            day=d-14
            fine=day*5
        books = list(models.Book.objects.filter(isbn=i.isbn))
        students = list(models.Student.objects.filter(user=i.student_id))
        i=0
        for l in books:
            t=(students[i].user,students[i].user_id,books[i].name,books[i].isbn,issuedBooks[0].issued_date,issuedBooks[0].expiry_date,fine)
            i=i+1
            details.append(t)
    return render(request, "view_issued_book.html", {'issuedBooks':issuedBooks, 'details':details})

def student_table(request):
    data = Student.objects.all()
    return render(request, "student_table.html", {'students':data})