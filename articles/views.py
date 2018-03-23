from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from searchbar import forms
# Create your views here.

#when views.article_list is called in url file this function is called
#render the html template

def article_list(request):
	# all the articles stored
	articles = Article.objects.all().order_by('date')
	return render(request, 'articles/article_list.html', {"articles": articles})

def article_detail(request, slug):
	# get the individual blog post where the slug equals the slug of the article
	# clicked on
	article = Article.objects.get(slug=slug)
	return render(request, 'articles/article_detail.html', {'article':article})

def articles_search(request):
	if request.method == 'GET':
		form = forms.SearchForm(request.GET, request.FILES)
		
		if form.is_valid():
			# this is the text typed into the search bar
			search_word = form.cleaned_data['title']
			# only get articles with titles that contain search word
			filtered_articles = Article.objects.filter(title__icontains=search_word)
			# if nothing matches your search display message
			if(filtered_articles):
				not_found =''
			else:
				not_found = "Sorry, no songs with that name have been posted."
			# return all needed information to article_search page	
			return render(request, 'articles/article_search.html', {"articles": filtered_articles,
				"search_word":search_word, "not_found": not_found})


