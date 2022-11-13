from django.shortcuts import render
from django.http import HttpResponse
from .models import Mobile
# Register your models here.

mobile_details = Mobile.objects.all()

def home(request):
    context={
        'mobile_details':mobile_details
    }
    return render(request,'mobile/home.html',context)
    # return HttpResponse('<h1>Mobile Home</h1>')



def about(request):
    return render(request,'mobile/about.html',{'title':'About'})
    # return HttpResponse('<h1>Mobile About</h1>')

def viewall(request):
    
    context={
        'mobile_details':mobile_details
    }
    return render(request,'mobile/viewall.html',context) 

def action_show_page(request):
    print(request.GET)
    return render(request, 'mobile/action_show_page.html')