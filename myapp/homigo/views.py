from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.conf import settings



PROJECT_NAME = getattr(settings, "PROJECT_NAME", "Unset Projet in Views")


# Create your views here.
def index(request):
    return render(request, 'index.html', {
        "project_name": PROJECT_NAME
    })

def health(request):
    return HttpResponse('ok')