from django.shortcuts import render,redirect
from django.http import HttpResponse
from dbapp.models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from dbapp.forms import EmpForm,Usersignupform,UserupdateForm,ProfileUpdateForm
from django.core.paginator import Paginator
# Create your views here.
def Home(request):
    return render(request,'dbapp/home.html')
@login_required
def Profile(request):
    if request.method=='POST':
        u_form=UserupdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'your account has benn updated')
            return redirect('dbapp:profile')
    else:
        u_form=UserupdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={'u_form':u_form,'p_form':p_form}
    return render(request,'dbapp/profile.html',context)

def Display(request,pno):
    emp=Employee.objects.all()
    p=Paginator(emp,5)
    page=p.get_page(pno)
    return render(request,'dbapp/display.html',{'emp':page})

def Signup(request):
    form=Usersignupform()
    if request.method=='POST':
        form=Usersignupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'registration/signup.html',{'form':form})
        
    return render(request,'registration/signup.html',{'form':form,})

def userlogin(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(request,username=uname,password=pwd)
        if user !=None:
            login(request,user)
            print(messages.success(request,'login successfull'))
            return redirect('home')
        else:
            messages.warning(request,'invalid user')
            return redirect('login')
    return render(request,'registration/login.html')

@login_required
def userlogout(request):
    logout(request)
    return redirect('login')


def empsearch(request):
    if request.method=='POST':
        empno=int(request.POST['empno'])
        emp_no=Employee.objects.filter(id=empno)
        print(emp_no)
        return render(request,'dbapp/search.html',{'emp':emp_no})
    
    return render(request,'dbapp/search.html')

def empcreate(request):
    emp=EmpForm()
    if request.method=='POST':
        emp=EmpForm(request.POST)
        if emp.is_valid():
            emp.save()
            return redirect('home')
        else:
            return render(request,'dbapp/create.html',{'emp':emp})      

    return render(request,'dbapp/create.html',{'emp':emp})

def empupdate(request,id):
    emp=Employee.objects.get(id=id)
    form=EmpForm(instance=emp)
    if request.method=='POST':
        form=EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'dbapp/update.html',{'form':form})

def empdelete(request,id):
    emp=Employee.objects.get(id=id)
    form=EmpForm(instance=emp)
    if request.method=='POST':
        emp.delete()
        return redirect('home')
    return render(request,'dbapp/delete.html',{'form':form})