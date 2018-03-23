from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls.static import static 
from django.conf import settings
from multiurl import multiurl
 

 #when the url is about/ call views.about function
 #when you django goes to articles/ it gets sent to the articles url.py file
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("articles.urls")),
    path('about/', views.about),
    
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)