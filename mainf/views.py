from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth import authenticate, login,logout

from .models import*
import requests
from django.http import JsonResponse
from django.contrib import messages
import requests


# Create your views here.
def Blogdetails(request,id):
    postdetail=BlogContent.objects.get(id=id)
    return render(request,"blog-details.html",{'postdetail':postdetail})

def index(request):
    return render(request,"index.html")

def Home(request):
    return render(request,"home.html")


def Club(request):
    return render(request,"club.html")

def Contact(request):
    return render(request,"contact.html")

def Result(request):
    return render(request,"result.html")

def Schedule(request):
    return render(request,"schedule.html")

def Home(request):
    return render(request,"Home.html")

# registrations


def Handle_Register(request):
    if request.method=="POST":
        username=request.POST['loginusername']
        email=request.POST['email']
        password=request.POST['loginpassword']
        user=User.objects.create_user(username,email,password)
        user.save()
        return redirect('signin')
    return render(request,'signup.html')



def Handle_Signin(request):
    if request.method=='POST':
        username=request.POST['loginusername']
        password=request.POST['loginpassword']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            return redirect('signin')
    return render(request,'registration.html')

def Handle_logout(request):
    logout(request)
    return redirect('index')




#blog 
def Handle_Blog(request):
  blog=BlogContent.objects.all()
  return render(request, 'blog.html', {'blogs': blog})

    




def SearchFunction(request):
    if request.method == "GET":
        query = request.GET.get('search')
        result1 = BlogContent.objects.filter(title__icontains=query)
        result2 = BlogContent.objects.filter(content__icontains=query)
        result3 = result1.union(result2)
        
        return render(request, 'search.html', {'result3': result3})
    else:
        return render(request, 'search.html')





