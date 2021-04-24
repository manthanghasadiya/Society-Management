from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.contrib import messages
from manageapp.models import guard_reg,user_reg,rent,addevent,guest,complain,maintain,Message, SendRecieve
from django.shortcuts import render, redirect
from .forms import rent_form,complain_form, maintain_form,addevent_form,guest_form
from time import sleep
from django.utils.datastructures import MultiValueDictKeyError
import mysql.connector
from operator import itemgetter
import json
from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from .serializers import MessageSerializer



@csrf_exempt
def message_list(request, sender=None, receiver=None):
    if request.method == 'GET':
        print(sender)
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        print(messages)
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = MessageSerializer(data=data)
        print(serializer)
        
        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



def chat_view(request,username):
    if request.method == "GET":
        try:
            data12=user_reg.objects.get(uname=username)
            data14=guard_reg.objects.all()

        except:
            data12=guard_reg.objects.get(uname=username)
            data14=user_reg.objects.all()

        
        try:
            data16=SendRecieve.objects.get(sr=data12.house)
            data15=SendRecieve.objects.exclude(sr=data12.house)
        except:
            data16=SendRecieve.objects.get(sr=data12.uname)
            data15=SendRecieve.objects.exclude(sr=data12.uname)

        context={"data12":data12,"data14":data14,"data15":data15,"data16":data16}
        return render(request, 'chat.html',context)  


def message_view(request, sender, receiver):
    
    if request.method == "GET":
        print(sender,receiver)
        data12=SendRecieve.objects.get(sr=receiver)
        data14=guard_reg.objects.all()
        data15=SendRecieve.objects.all()
        data16=SendRecieve.objects.get(sr=sender)
        context={'users': SendRecieve.objects.exclude(sr=sender),
                       'receiver': SendRecieve.objects.get(sr=receiver),
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender),
                                   "data12":data12,"data14":data14,"data15":data15,"data16":data16}
        print(context)
        return render(request, "message.html",context)
                      



def login(request):
    con=mysql.connector.connect(host="localhost",user="socmansys",password="bdms",database="managesys")
    cursor=con.cursor()
    con2=mysql.connector.connect(host="localhost",user="socmansys",password="bdms",database="managesys")
    cursor2=con2.cursor()
    con3=mysql.connector.connect(host="localhost",user="socmansys",password="bdms",database="managesys")
    cursor3=con3.cursor()
    con4=mysql.connector.connect(host="localhost",user="socmansys",password="bdms",database="managesys")
    cursor4=con4.cursor()
    sqlcmd="SELECT uname FROM managesys.manageapp_user_reg"
    sqlcmd2="SELECT password FROM managesys.manageapp_user_reg"
    sqlcmd3="SELECT uname FROM managesys.manageapp_guard_reg"
    sqlcmd4="SELECT password FROM managesys.manageapp_guard_reg"
    cursor.execute(sqlcmd)
    cursor2.execute(sqlcmd2)
    cursor3.execute(sqlcmd3)
    cursor4.execute(sqlcmd4)

    uu=[]
    up=[]
    gu=[]
    gp=[]
    
    for i in cursor:
        uu.append(i)
    for i in cursor2:    
        up.append(i)
    for i in cursor3:    
        gu.append(i)
    for i in cursor4:    
        gp.append(i)
       
    res=list(map(itemgetter(0),uu))
    res2=list(map(itemgetter(0),up))
    res3=list(map(itemgetter(0),gu))
    res4=list(map(itemgetter(0),gp))
    print(res)
    print(res3)
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['password']
        i=j=0
        k=len(res)
        k2=len(res3)
        if username=='0' and password=='0':
            return homeadmin(request)
        
        else:
            while i<k:
                print(res[i])
                if res[i]==username and res2[i]==password:
                    print(res[i])
                    return homeuser(request, username)
                    break
                i+=1   
            while j<k2:
                print(res3[j])

                if res3[j]==username and res4[j]==password:
                    print(res3[j])
                    
                    return homeguard(request,username)
                    break
                j+=1

    return render(request, 'login.html')


def signup(request):
    return render(request, 'Sign_up.html')

def index(request):
    return render(request, 'index.html')

def rec(request,username):
    data20=user_reg.objects.get(uname=username)
    data21=maintain.objects.all()
    context={"data20":data20, "data21":data21}
    for i in data21:
        if i.Name==username:
            return render(request, 'rec.html', context)
        else:
            pass
    return homeuser(request,username)

def homeuser(request, username):
    data2=user_reg.objects.get(uname=username)
    context={"username":username,"data2": data2}
    return render(request, 'homeuser.html',context)

def homeguard(request, username):
    data98=guard_reg.objects.all()
    context={"username":username}
    return render(request, 'homeguard.html',context)    

def homeadmin(request):
    return render(request, 'homeadmin.html')

def help(request,username):
    data60=user_reg.objects.get(uname=username)
    context={"data60":data60}
    return render(request, 'help.html', context)

def profile(request,username):
    print(username)
    data9=user_reg.objects.get(uname=username)
    context={"data9":data9}
    return render(request, 'profile.html',context)    

def residentd(request):
    data4=user_reg.objects.all()
    context={"data4":data4}
    return render(request, 'residentd.html',context)

def guardd(request):
    data5=guard_reg.objects.all()
    context={"data5":data5}
    return render(request, 'guardd.html',context)

def rentd(request):
    if request.method=='POST':
         month=request.POST.get("search")
         print(month)
         data61=rent.objects.all()
         data6=rent.objects.filter(Month=month)
         if month=='All':
            context={"data6":data61}
         else:             
            context={"data6":data6}
         print(data6)
         return render(request, 'rentd.html',context)

    return render(request, 'rentd.html')


def maind(request):
    
    if request.method=='POST':
         month=request.POST.get("search")
         print(month)
         data7=maintain.objects.all()
         data4=maintain.objects.filter(Month=month)
         if month=='All':
             print("all")
             context={"data7":data7,"data4":data7}
         else:
            context={"data7":data7,"data4":data4}
         print(data4)
         return render(request, 'maind.html',context)

    return render(request, 'maind.html')

def cdetail(request):
    data8=complain.objects.all()
    context={"data8":data8}
    return render(request, 'cdetail.html',context)

def eventd(request,username):
    data10=addevent.objects.all()
    data90=user_reg.objects.get(uname=username)
    context={"data10":data10,"data90":data90}
    return render(request, 'eventd.html',context)

def guestd(request):
    data11=guest.objects.all()
    context={"data11":data11}
    return render(request, 'guestd.html',context)

def lpd(request, username):
    data90=user_reg.objects.get(uname=username)
    data91=user_reg.objects.get(uname=username)
    print(data91)
    if data91.Option=='Home':
       data11=maintain.objects.filter(Name=username)
       print(data11)
       print("1")
    else:
       data11=rent.objects.filter(Name=username)
       print(data11)
       print("2")

    context={"data11":data11,"data90":data90}
    return render(request, 'lpd.html',context)

def uge(request, username):
    data19=user_reg.objects.get(uname=username)
    print(data19)
    data80=guest.objects.filter(house_id=data19)
    print(data80)
    context={"data80":data80,"data19":data19}
    return render(request, 'uge.html',context)

def addevents(request):
    if request.method=='POST':
        form=addevent_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'homeadmin.html')
        else:
            print(form.errors)
    return render(request, 'addevent.html')

def complainbox(request, username):
    data40=user_reg.objects.get(uname=username)
    context={"data40":data40}  
    if request.method=='POST':
        print("1complain")
        form=complain_form(request.POST)
        if form.is_valid():
            print("2complain")
            form.save()
            print("3complain")
            return complainbox(request, username)
        else:
            print(form.errors)
              
    return render(request, 'complain.html',context) 

def complainboxg(request, username):
    data95=guard_reg.objects.get(uname=username)
    context={"data95":data95}
    if request.method=='POST':
        form=complain_form(request.POST)
        if form.is_valid():
            form.save()
            return homeguard(request, username)
        else:
            print(form.errors)
            
    return render(request, 'complaing.html',context) 

def maintainpay(request,username):
    data3=user_reg.objects.all()
    data57=user_reg.objects.get(uname=username)
    context={"data3":data3,"data57":data57}
    if request.method=='POST':
        form=maintain_form(request.POST)
        if form.is_valid():
            form.save()
            return homeuser(request, username)
        else:
            print(form.errors)
    
    return render(request, 'maintain.html',context)

def rentpay(request,username):
    data=user_reg.objects.all()
    data56=user_reg.objects.get(uname=username)
    context={"data":data,"data56":data56}
    if request.method=='POST':
        form=rent_form(request.POST)
        if form.is_valid():
            form.save()
            return homeuser(request, username)
        else:
            print(form.errors)
    
    return render(request, 'rent.html',context)  


def addguest(request, username):
    data60=guard_reg.objects.get(uname=username)
    context={"data60":data60}  
    if request.method=='POST':
        form=guest_form(request.POST)
        if form.is_valid():
            form.save()
            return homeguard(request, username)
        else:
            print(form.errors)
    
        
    return render(request, 'addguest.html',context)        

def userreg(request):
    
    if request.method=='POST':
        
        print("Hello")
        
        uname=request.POST.get('uname')
        fname=request.POST.get('fname')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        mobile=request.POST.get('mobile')
        house=request.POST.get('house')
        Option=request.POST.get('Option')
        password=request.POST.get('password')
        # sleep(0.5)
        if uname != None:
            print(uname,fname,mobile,password)    
            ins=user_reg()
            ins.uname=uname
            ins.fname=fname
            ins.mname=mname
            ins.lname=lname
            ins.mobile=mobile
            ins.house=house
            ins.Option=Option
            ins.password=password
            ins.save()
            obj=SendRecieve()
            obj.sr=house
            obj.save()

            print("The data is store")
            return redirect('http://localhost:8000')
            # return render(request, 'login.html')
    return render(request, 'Sign_up_user.html')

def guardreg(request):
    if request.method=='POST':
        
        print("Hello")
        
        uname=request.POST.get('uname')
        fname=request.POST.get('fname')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        # sleep(0.5)
        if uname != None:
            print(uname,fname,mobile,password)    
            ins=guard_reg()
            ins.uname=uname
            ins.fname=fname
            ins.mobile=mobile
            ins.password=password
            ins.save()
            obj=SendRecieve()
            obj.sr=uname
            obj.save()
            print("The data is store")
            return redirect('http://localhost:8000')
            # return render(request, 'login.html')

    return render(request, 'Sign_up_guard.html')