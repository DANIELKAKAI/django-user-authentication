from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import MyUser


@login_required(login_url='signin')
def index(request):
	user = request.user
	return render(request,"myapp/index.html",{'user':user})



def signup(request):
	if request.method =='POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = MyUser.objects.create_user(email=email,password=password,role='basic')
		user.save()
		login(request,user)
		return redirect('index')
	return render(request,"myapp/signup.html")





def signin(request):
	if request.method =='POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(email=email,password=password)
		if user:
			login(request,user)
			return redirect('index')
	return render(request,"myapp/signin.html")



def signout(request):
	logout(request)
	return redirect('signin')
