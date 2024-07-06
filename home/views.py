from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Poster,CustomerClub
def home_page(request):
    poster=Poster.objects.filter(is_active=True)
    context={
        "poster":poster,
    }
    return render(request,"home_page.html",context)

def get_emails(request):
    if request.method=="POST":
        email=request.POST.get('email')
        cs_before=CustomerClub.objects.all()
        cs_before=list(cs_before)
        flag=0
        for i in cs_before:
            if str(i)==email:
                flag=1
                break
        if flag == 0:
            cs=CustomerClub.objects.create(email=email)
            cs.save()
            success="با موفقیت ثبت شد"
            return success
        else:
            error="این ایمیل قبلا وارد شده است"
            return error

def header_page(request):
    return render(request,'header.html')

def footer_page(request):
    if request.method=="POST":
        message=get_emails(request)
        print(message)
    message=''
    context={
        "message":message,
    }
    return render(request,'footer.html',context)