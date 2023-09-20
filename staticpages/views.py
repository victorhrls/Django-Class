from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.urls import include, path # modificar esta linha    
# Create your views here.

urlpatterns = [
    path('staticpages/', include('staticpages.urls')), # adicionar esta linha
    path('admin/', admin.site.urls),
]



def index(request):
    context = {}
    return render(request, 'staticpages/index.html', context)


def about(request):
    context = {}
    return render(request, 'staticpages/about.html', context)