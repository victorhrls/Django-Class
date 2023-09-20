from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.urls import include, path # modificar esta linha    
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello World!</h1>")

urlpatterns = [
    path('staticpages/', include('staticpages.urls')), # adicionar esta linha
    path('admin/', admin.site.urls),
]