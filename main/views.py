from django.http import JsonResponse
from django.shortcuts import render
from .models import Cafe
import datetime
import json

def index(request):
    return render(request, 'main/index.html')

def cafelist(request):
    cafelistobj = Cafe.objects.all()
    return render(request, 'main/cafelist.html', {'cafelistobj':cafelistobj})

f = open("/workspace/mmri/mysite/mysite/static/food.csv", 'r')
l = []
lines = f.readlines()
for line in lines:
    l.append(line.split(','))
f.close()

data = l[1:44]


def restau_list(request):
    return render(request, 'main/restau_list.html', {'data':data})
#    return render(request, 'main/restau_list.html', {'data':data})

def event(request):
    return render(request, 'main/event.html')

def review(request):
    return render(request, 'main/review.html')

def cafedetails(request, pk):
    cafeobj = Cafe.objects.get(pk=pk)
    return render(request, 'main/cafedetails.html', {'cafeobj':cafeobj})

def sample(request):
    value = 'CEO Goh'
    sampleText = '''Wow
    CEO
    goh
    '''
    l = [1, 2, 3]
    dateT = datetime.datetime.now()
    return render(request, 'main/sample.html', {'value':value, 'dateT':dateT, 'sampleText':sampleText, 'l':l})

# Create your views here.
