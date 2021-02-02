from django.shortcuts import render,redirect
from store.models.signup import Signupm
from store.models.signup import Signupm
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.views import View

class Login(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
           uname = request.POST.get('uname')
           password = request.POST.get('password')
           try:
             user = Signupm.objects.get(username=uname)
           except:
             messages.error(request,"The username is not exists!!")
             return render(request,'login.html')
           a = check_password(password,user.password1)
           if a==True:
             messages.success(request,"You have loged in successfully!!")
             request.session['customer']=user.id
             request.session['username']=user.username
             print('Hello',request.session.get('username'))
             return redirect("/")
           else:
             messages.error(request,"You have entered wrong password!!")
             return render(request,'login.html')

def logout(request):
  request.session.clear()
  return redirect('login')