# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from django.shortcuts import render
from .models import Education
from .models import Experience
from .models import Awards
from .models import Projects
from .models import Blog
# Create your views here.

def index(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    awards = Awards.objects.all()
    projects = Projects.objects.all()
    blogs = Blog.objects.all()

    return render(request, 'index.html', {'education': education,'experience':experience,'awards':awards,'projects':projects,'blogs':blogs})