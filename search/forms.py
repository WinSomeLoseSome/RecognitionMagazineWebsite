from django import forms
from articles import models

class SearchForm(forms.ModelForm):
	class Meta:
		model = models.Article
		fields = ['title', 'quote'] 