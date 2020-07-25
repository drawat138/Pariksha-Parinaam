from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile, Vacancy
def index(request):
	return HttpResponse("<h1> WELCOME TO MY WEBSITE </h1>")

def jobs(request):
		vacancy= Vacancy.objects.all()
		context= {'vacancy':vacancy}
		return render(request,'home/jobs.html',context)

def detail(request,id):
	vacancy=Vacancy.objects.get(id=id)
	context={'vacancy':vacancy}
	return render(request,'home/detail.html',context)
def result(request):
	return render(request,'home/result.html')
def admitcard(request):
	return render(request,'home/admitcard.html')
def answerkey(request):
	return render(request,'home/answerkey.html')




# def user_profile(request): 
# 	form=RegistrationForm(request.POST or None)
# 	if request.method=="POST":
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/home')
# 	context={'form':form}
# 	return render(request,'home/home.html',context)



