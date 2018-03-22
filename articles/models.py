from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length =100) 
	slug = models.SlugField()
	quote = models.CharField(max_length=200)
	artist = models.CharField(default='Unknown', max_length=200)
	producer = models.CharField(default='Unknown', max_length=200)
	vocals_body = models.TextField(default='N/A')
	beat_body = models.TextField(default='N/A')
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png', blank=True)
	embed = models.TextField(default='')

	#add in author later
	
	def __str__(self):
		return self.title;

	def snippet(self):
		if (len(self.vocals_body) <= 50):
			return self.vocals_body
		else:
			return self.vocals_body[:50] + '...'

	
		
		