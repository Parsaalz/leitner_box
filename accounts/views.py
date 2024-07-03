from django.shortcuts import render,redirect
from .forms import Login_Page_Form,signup_page_Form,ForgetPasswordForm,ResetPasseord
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Image_Users,Moreinformation
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
from django.conf import settings
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
                us_n=Moreinformation.objects.filter(user=user_n).first()
                print(us_n,1)
                if us_n.changepass==True:
                    return redirect("reset_password",user_id=user_n.id)
                login(request,user_n)
                us_n=Moreinformation.objects.get(user=user_n)
                return redirect('home_page')
            else:
                fr.add_error("password","نام کاربری یا رمز عبور صحیح نیست")
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
            user=User.objects.get(username=username_t)
            image=Image_Users.objects.create(user=user,image='images/images.png')
            user_more_info=Moreinformation.objects.create(user=user)
            user_more_info.save()
            messages.success(request, 'با موفقیت ثبت نام کردید.')
            return redirect("login_page")
    context={
        "sg":sg,
    }
    return render(request,"signup_page.html",context)


def forget_password(request):
    form=ForgetPasswordForm()
    if request.method=="POST":
        form=ForgetPasswordForm(data=request.POST)
        if form.is_valid():
            email_t=form.cleaned_data.get('email')
            email_validate=User.objects.filter(email=email_t).first()
            if email_validate:
                code=get_random_string(40)
                email = EmailMessage(
                "بازیابی رمز عبور",
                code,
                settings.EMAIL_HOST_USER,
                [email_t],
                ).send()
                user_n=User.objects.get(email=email_t)
                user_n.set_password(code)
                user_n.save()
                change_p=Moreinformation.objects.get(user=user_n)
                change_p.changepass=True
                change_p.save()
                return redirect('login_page')
            else:
                form.add_error("email","این ایمیل وجود ندارد")
    context={
        "form":form,
    }
    return render(request,'forget_password.html',context)

def reset_password(request,user_id):
    form=ResetPasseord()
    if request.method=="POST":
        form=ResetPasseord(data=request.POST)
        if form.is_valid():
            password2=form.cleaned_data.get('confirm_password')
            user_n=User.objects.get(id=user_id)
            user_n.set_password(password2)
            user_n.save()
            user_more=Moreinformation.objects.get(user=user_n)
            user_more.changepass=False
            user_more.save()
            email_t=user_n.email
            email = EmailMessage(
                "بازیابی رمز عبور",
                "رمز عبور شما تغییر یافت",
                settings.EMAIL_HOST_USER,
                [email_t],
                ).send()
            return redirect('login_page')
    context={
        "form":form,
    }
    return render(request,'reset_pass.html',context)