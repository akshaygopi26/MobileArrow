from django.shortcuts import render
from django.http import HttpResponse
from .models import Mobile
from django.db.models import Q
from django.db.models import Max

from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

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

class Viewall(ListView):
    model=Mobile
    template_name='mobile/viewall.html' 
    context_object_name='mobile_details'
    extra_context={
        'brands' :Mobile.objects.values('brand').distinct(),
        'ram' :Mobile.objects.values('RAM').distinct()}
    paginate_by=5


def viewall(request):
    mobile_details = Mobile.objects.all()
    print(Mobile.objects.values('RAM').distinct())
    context={
        'mobile_details':mobile_details,
        'brands' :Mobile.objects.values('brand').distinct(),
        'ram' :Mobile.objects.values('RAM').distinct()
    }
    return render(request,'mobile/viewall.html',context) 



def action_show_page(request):
    print(request.GET)
    pricerange=request.GET['price']
    if (pricerange=='none'):
        maxprice=Mobile.objects.aggregate(Max('sales_price'))
        price=[0,maxprice]
    else:
        price=pricerange.split('-')
        if price[1]=='':
            maxprice=Mobile.objects.aggregate(Max('sales_price'))
            price[1]=maxprice
            price[1]=100000
    
    brand=request.GET['brand']
    if(brand=='none'):
        brand=Mobile.objects.values_list('brand').distinct()
        brandlist=[]
        for b in brand:
            brandlist.append(b[0])
        brand=brandlist
    else:
        brandlist=[]
        brandlist.append(brand)
        brand=brandlist

    ram=request.GET.getlist('RAM')
    if len(ram)==0:
        ram=Mobile.objects.values_list('RAM').distinct()
        ramlist=[]
        for r in ram:
            ramlist.append(r[0])
        ram=ramlist
    
    if(request.GET['battery']=='none'):
        maxbat=Mobile.objects.aggregate(Max('battery_capacity'))
        battery=[0,maxbat]
    else:
        battery=request.GET['battery'].split('-')
        if(battery[1]==''):
            maxbat=Mobile.objects.aggregate(Max('battery_capacity'))
            battery[1]=maxbat
    print(price)
    print(Mobile.objects.filter(Q(RAM__in=ram)).values())
    context={

        'mobile_details':Mobile.objects.filter(
            Q(brand__in=brand) & 
            Q(sales_price__range=(price[0],price[1]))&
            Q(RAM__in=ram) &
            Q(battery_capacity__range=(battery[0],battery[1]))).values(),

        'brands' :Mobile.objects.values('brand').distinct(),
        'ram' :Mobile.objects.values('RAM').distinct()
    }
    return render(request, 'mobile/viewall.html',context)


def action_compare_page(request):
    ids=request.GET.getlist('model')
    context={
        'mobile_detail1':Mobile.objects.filter(id=ids[0]).values(),
        'mobile_detail2':Mobile.objects.filter(id=ids[1]).values(),
        
    }
    return render(request, 'mobile/compare_display.html',context)

class MobileDetailView(DetailView):
    model=Mobile


class Compare(ListView):
    model=Mobile



def compare(request):

    context={
        'mobilenames1' :Mobile.objects.values()
        
    }
    return render(request, 'mobile/compare.html',context)
