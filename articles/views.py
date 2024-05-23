from django.shortcuts import render
from .models import Articles_page
def articles_page(request):
    ar=Articles_page.objects.all()
    context={
        "ar":ar,
    }
    return render(request,'articles_page.html',context)
