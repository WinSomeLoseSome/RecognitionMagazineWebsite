from django import forms
from articles import models

class SearchForm(forms.ModelForm):
	# for styling - removes label and add placeholder
	title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Search'}))
	# model form set up with only title field
	class Meta:
		model = models.Article
		fields = ['title'] 