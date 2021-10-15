from django.core import paginator
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from datetime import datetime
from mapapp.models import maplist
from django.contrib import auth
from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger

# Create your views here.
def index(request):
    all=maplist.objects.all()
    return render(request,'index.html',locals())

def login(request):
    messages=''
    if request.method=='POST':
        name=request.POST['username'].strip()
        password=request.POST['password']
        user1=authenticate(username=name,password=password)
        if user1.is_active:
            auth.login(request,user1)
            return redirect('/adminmain/')
        else:
            messages="Account hasn,t regist"
    else:
        messages='Login Error'
    return render(request,'login.html',locals())
def logout(request):
    auth.logout(request)
    return redirect('/index/')

def adminmain(requset):
    map_list=maplist.objects.all().order_by('-id')
    paginator=Paginator(map_list,6)#every page fields number
    page=requset.GET.get('page')
    try:
        maps=paginator.page(page)
    except PageNotAnInteger:#list first page
        maps=paginator.page(1)
    except EmptyPage:#list last page
        maps=paginator.page(paginator.num_pages)
    return render(requset,'adminmain.html',locals())
def adminadd(request):
    if('mapName' in request.POST):#press confirm button
        name=request.POST['mapName']
        desc=request.POST['mapDesc']
        lat=request.POST['mapLat']
        lng=request.POST['mapLng']
        tel=request.POST['mapTel']
        addr=request.POST['mapAddr']
        rec=maplist(mapName=name,mapDesc=desc,mapLat=lat,mapLng=lng,mapTel=tel,mapAddr=addr)
        rec.save()
        return redirect('/adminmain/')
    return render(request,'adminadd.html',locals())

def adminedit(request,editid=None):
    if editid !=None:
        rec=maplist.objects.get(id=editid)
        return render(request,"adminedit.html",locals())
    else:
        editid1=request.POST['editid']
        rec=maplist.objects.get(id=editid1)
        rec.mapName=request.POST['mapName']
        rec.mapDesc=request.POST['mapDesc']
        rec.mapLat=request.POST['mapLat']
        rec.mapLng=request.POST['mapLng']
        rec.mapTel=request.POST['mapTel']
        rec.mapAddr=request.POST['mapAddr']
        rec.save()
        return redirect('/adminmain/')

def admindelete(request):
    delid=request.get['id']
    rec=maplist.objects.get(id=delid)
    rec.delete()
    return redirect('/adminmain/')