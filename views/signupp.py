from django.shortcuts import render
from store.models.signup import Signupm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views import View

class Signupp(View):
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self,request):
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(uname)<3 or uname.isalpha()!=True or uname.isspace()==True:
           messages.error(request,"Please enter minimum 3 alpha charcters only and ensure there is no space in between!!")
           return render(request,'signup.html')
        
        elif len(fname)<4 or fname.isalpha()!=True or lname.isspace()==True:
            messages.error(request,"Please enter minimum 4 alpha charcters only and ensure there is no space in between!!")
            return render(request,'signup.html')

        elif len(fname)<3 or fname.isalpha()!=True or fname.isspace()==True:
            messages.error(request,"Please enter minimum 3 alpha charcters only and ensure there is no space in between!!")
            return render(request,'signup.html')  
        
        elif len(mobile)<10 or len(mobile)>10 or mobile.isdigit()!=True or mobile.isspace()==True: 
            messages.error(request,"Please enter minimum 10 numeric digits only and ensure there is no space in between!!")
            return render(request,'signup.html')

        elif len(password1) <7 or password1.isspace()==True: 
            messages.error(request,"Please enter minimum 7 charcters and ensure there is no space in between!!")
            return render(request,'signup.html')
        
        elif (password2!=password1): 
            messages.error(request,"Please enter same password and ensure there is no space in between!!")
            return render(request,'signup.html')

        elif Signupm.objects.filter(username=uname).exists():
            messages.error(request,"The username is already exists!!")
            return render(request,'signup.html')         
        else:
           Signupm.objects.create(username=uname,firstName=fname,lastName=lname,
           mobile=mobile,email=email,password1=make_password(password1),password2=make_password(password2))
           messages.success(request,"Your Account Created Successfully!!")
           return render(request,'signup.html')