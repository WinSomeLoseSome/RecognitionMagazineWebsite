from . import forms

def search_form(request):
	return {'search_form' : forms.SearchForm()}