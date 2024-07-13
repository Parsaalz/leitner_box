from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Poster,CustomerClub
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import PosterSerializer
from rest_framework import status
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

@api_view(['GET','POST'])
def my_api(request):
    if request.method == 'GET':
        poster=Poster.objects.all()
        serializer=PosterSerializer(poster,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method =="POST":
        serializer=PosterSerializer(data=request.data)
        if serializer.is_valid():
            title=serializer.validated_data.get('title')
            short_description=serializer.validated_data.get('short_description')
            url_title=serializer.validated_data.get('url_title')
            url=serializer.validated_data.get('url')
            image=serializer.validated_data.get('image')
            is_active=serializer.validated_data.get('is_active')
            created_date=serializer.validated_data.get('created_date')
            article=Poster.objects.create(title=title,short_description=short_description,url_title=url_title,url=url,image=image,is_active=is_active,created_date=created_date)
            article.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE'])    
def my_api_detail(request,id):
    poster=Poster.objects.get(id=id)
    if request.method == 'GET':
        serializer=PosterSerializer(poster)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=="DELETE":
        poster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)