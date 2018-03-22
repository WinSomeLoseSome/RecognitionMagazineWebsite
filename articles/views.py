from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.

#when views.article_list is called in url file this function is called
#render the html template
def article_list(request):
	articles = Article.objects.all().order_by('date')
	return render(request, 'articles/article_list.html', {"articles": articles})

def article_detail(request, slug):
	#return HttpResponse(slug)
	article = Article.objects.get(slug=slug)
	return render(request, 'articles/article_detail.html', {'article':article})