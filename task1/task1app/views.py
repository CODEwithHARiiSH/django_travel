from django.shortcuts import render
from django.http import HttpResponse
from .models import team , destinations

# Create your views here.

def fun(request):
    var = team.objects.all()
    var1 = destinations.objects.all()
    return render(request,'index.html', {'res':var , 'res1':var1})
