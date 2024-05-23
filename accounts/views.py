from django.shortcuts import render,redirect
from .forms import Login_Page_Form,signup_page_Form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
import time
def login_page(request):
    fr=Login_Page_Form()
    if request.method == "POST":
        fr=Login_Page_Form(data=request.POST)
        if fr.is_valid():
            username_t=fr.cleaned_data.get('username')
            password_t=fr.cleaned_data.get("password")
            user_n=authenticate(request,username=username_t,password=password_t)
            if user_n is not None:
                login(request,user_n)
                return redirect('home_page')
    context={
        "fr":fr,
    }
    return render(request,'login_page.html',context)


def logout_page(request):
    logout(request)
    return redirect("home_page")

def signup_page(request):
    sg=signup_page_Form()
    if request.method=='POST':
        sg=signup_page_Form(data=request.POST)
        if sg.is_valid():
            username_t=sg.cleaned_data.get('username')
            password_t=sg.cleaned_data.get('password')
            confirmation_t=sg.cleaned_data.get('confirmation')
            firstname_t=sg.cleaned_data.get('firstname')
            lastname_t=sg.cleaned_data.get('lastname')
            email_t=sg.cleaned_data.get('email')
            user=User.objects.create_user(username=username_t,password=confirmation_t)
            user.email=email_t
            user.first_name=firstname_t
            user.last_name=lastname_t
            user.save()
            messages.success(request, 'با موفقیت ثبت نام کردید.')
            time.sleep(3)
            return redirect("login_page")
    context={
        "sg":sg,
    }
    return render(request,"signup_page.html",context)

