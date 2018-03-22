
from django.shortcuts import render
from articles import models
from django.http import HttpResponse
from . import forms
# Create your views here.

#when views.article_list is called in url file this function is called
#render the html template
def search(request):
	form = forms.SearchForm()
	return render(request, "search_bar/search_bar.html", {'form':form})
