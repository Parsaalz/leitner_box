from django.shortcuts import render,redirect
from .models import Articles_page,ArticlesComment,Category_Articles
from django.core.paginator import Paginator
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