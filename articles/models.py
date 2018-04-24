from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length =100) 
	slug = models.SlugField()
	quote = models.CharField(max_length=200)
	artist = models.CharField(default='Unknown', max_length=200)
	producer = models.CharField(default='Unknown', max_length=200)
	genre = models.CharField(default=None, blank=True, null=True, max_length=200)
	vocals_body = models.TextField(default=None, blank=True, null=True)
	beat_body = models.TextField(default=None, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	album_art = models.ImageField(default='default.png', blank=True)
	artist_image = models.ImageField(default=None, blank=True, null=True)
	embed = models.TextField(default=None, blank=True, null=True)
	author = models.CharField(default='Unknown', max_length=200)
	#add in author later
	
	def __str__(self):
		return self.title;

	def snippet(self):
		if (len(self.vocals_body) <= 400):
			return self.vocals_body
		else:
			return self.vocals_body[:400] + '...'

	
	
		
		