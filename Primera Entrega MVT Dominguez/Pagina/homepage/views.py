from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

# Create your views here.
from .models import Familiar

def inicio(request):

      return render(request, "homepage/inicio.html")

def familias(request):
  familiars_list = Familiar.objects.all()
  context = {'familiars_list': familiars_list}
  return render(request, 'homepage/familias.html', context=context)