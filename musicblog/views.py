from django.http import HttpResponse
from django.shortcuts import render
from articles import models



def home(request):
	#return HttpResponse("homepage")
	return render(request, "home.html")

def about(request):
	#return HttpResponse("about")
	return render(request, "about.html")

def contact(request):
	#return HttpResponse("about")
	return render(request, "contact.html")