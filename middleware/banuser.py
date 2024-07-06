from accounts.models import banusers
from django.http import HttpResponse,HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth import logout
class BanUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ban=[]
        if request.user.is_authenticated:
            ban=banusers.objects.filter(username=request.user.id)
        if len(ban)!=0:
            logout(request)
            return render(request,'eror_banusers.html')
        
        response = self.get_response(request)
        return response

