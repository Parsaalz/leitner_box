from django.shortcuts import render,redirect
from .models import Articles_page,ArticlesComment,Category_Articles
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticlesSerializers
from rest_framework import status
def articles_page(request):
    categorys=Category_Articles.objects.all()
    if request.GET.get('category'):
        category_title=request.GET.get('category')
        articles=Articles_page.objects.filter(published='p',category__name=category_title)
    else:
        articles=Articles_page.objects.filter(published='p')
    articles_paginate=Paginator(articles,6)
    page_number = request.GET.get("page")
    page_obj = articles_paginate.get_page(page_number)
    context={
        "articles":page_obj,
        "categorys":categorys,
    }
    return render(request,'articles_page.html',context)


def detals_articles(request,id):
    ar=Articles_page.objects.get(id=id)
    if request.method=="POST":
        comment_email=request.POST.get('email_commment')
        new_comment=ArticlesComment.objects.create(article=ar,parent=None,text=comment_email,user=request.user)
        new_comment.save()
        return redirect('detail_page',id=id)
    comment=ArticlesComment.objects.filter(article__id=id,parent=None).prefetch_related('articlescomment_set')
    context={
        "article":ar,
        "comments":comment,
    }
    return render(request,"detailpage.html",context)

@api_view(['GET',"POST"])
def api_articles(request):
    if request.method=="GET":
        articles=Articles_page.objects.all()
        serializers=ArticlesSerializers(articles,many=True)
        return Response(serializers.data)
    elif request.method=="POST":
        serializer=ArticlesSerializers(data=request.data)
        if serializer.is_valid():
            title=serializer.validated_data.get('title')
            short_description=serializer.validated_data.get('short_description')
            image=serializer.validated_data.get('image')
            author_name=serializer.validated_data.get('author_name')
            description=serializer.validated_data.get('description')
            published=serializer.validated_data.get('published')
            created_date=serializer.validated_data.get('created_date')
            articles_new=Articles_page.objects.create(title=title,short_description=short_description,image=image,author_name=author_name,description=description,published=published,created_date=created_date)
            category=request.data.get('category')
            for category_id in category:
                cat=Articles_page.objects.get(id=category_id)
                articles_new.category.add(cat)
            return Response(request.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)