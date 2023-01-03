from django.shortcuts import render,redirect
from django.views import View
from . forms import Employeeform
from . models import Employe
from django.contrib.auth.models import User

# Create your views here.
class Employeesignup(View):
    def get(self,request):
        signup=Employeeform()
        d={'signup':signup}
        return render(request,'signup.html',d)
    def post(self,request):
        signup=Employeeform(request.POST)
        if signup.is_valid():
            Name=signup.cleaned_data['Name']
            Email=signup.cleaned_data['Email']
            Password=signup.cleaned_data['Password']
            Designation=signup.cleaned_data['Designation']
        user=User.objects.create_user(username=Name,email=Email,password=Password) 
        user.designation=Designation
        user.save()
        return redirect('signup')

