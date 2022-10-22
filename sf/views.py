from http.client import HTTPResponse
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.views import View

from .models import User
from.forms import MyLoginForm, StudentRegistation
from django.contrib.auth import authenticate,login
# Create your views 
# here.
def home(request):
    return render(request,'enroll/home.html')
def add_show(request):
    if request.method == 'POST':
        fm= StudentRegistation(request.POST)
        if fm.is_valid():
            fn=fm.cleaned_data['first_name']
            lm=fm.cleaned_data['last_name']
            cp=fm.cleaned_data['confirm_password']
            pr=fm.cleaned_data['profile_picture']
            nm=fm.cleaned_data['username']
            em= fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            reg=User(username=nm,email=em,password=ps,confirm_password=cp,profile_picture=pr,first_name=fn,last_name=lm)
            reg.save()
            fm= StudentRegistation()

    else:
        fm= StudentRegistation()



    stn=User.objects.all()

    return render(request, 'enroll/adsh.html',{'fm':fm,'stn':stn})

class MyloginView(View):
    def get(self,request):
        fm =MyLoginForm()
        return render(request,'enroll/login.html',{'form':fm})
    def post(self,request):
        fm= MyLoginForm(request,data=request.POST)
        if fm.is_valid():
            username =fm.cleaned_data['username']
            password= fm.cleaned_data['password']
            user= authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return render(request,'enroll/login.html',{'form':fm})
        else:
            return render(request,'enroll/login.html',{'form':fm})



def delete_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk= id)
        pi.delete()
        return HttpResponseRedirect('/')

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, '<sf>/upst.html', {"user":user})