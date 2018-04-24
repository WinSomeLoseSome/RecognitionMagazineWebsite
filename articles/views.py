from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from searchbar import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

#when views.article_list is called in url file this function is called
#render the html template

def article_list(request):
	# all the articles stored
	articles_list = Article.objects.all().order_by('-date')
	page = request.GET.get('page', 1)

	paginator = Paginator(articles_list, 4)
	try: 
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	return render(request, 'articles/article_list.html', {"articles": articles})

def article_detail(request, slug):
	# get the individual blog post where the slug equals the slug of the article
	# clicked on
	article = Article.objects.get(slug=slug)
	return render(request, 'articles/article_detail.html', {'article':article})

def articles_search(request):
	if request.method == 'GET':
		form = forms.SearchForm(request.GET, request.FILES)
		
		if form.is_valid() or not form.is_valid():
			# this is the text typed into the search bar
			search_word = form.cleaned_data['title']
			# only get articles with titles that contain search word
			filtered_articles = Article.objects.filter(title__icontains=search_word)
			# if nothing matches your search display message
			if(filtered_articles):
				not_found =''
			else:
				not_found = "Sorry, no songs with that name have been posted."

			page = request.GET.get('page', 1)

			paginator = Paginator(filtered_articles, 50)
			try: 
				articles = paginator.page(page)
			except PageNotAnInteger:
				articles = paginator.page(1)
			except EmptyPage:
				articles = paginator.page(paginator.num_pages)
			# return all needed information to article_search page	
			return render(request, 'articles/article_search.html', {"articles": articles,
				"search_word":search_word, "not_found": not_found})


