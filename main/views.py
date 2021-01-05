from django.http import JsonResponse
from django.shortcuts import render
from .models import Cafe
from django.conf import settings
import datetime
import json

def index(request):
    return render(request, 'main/index.html')

def cafelist(request):
    cafelistobj = Cafe.objects.all()
    return render(request, 'main/cafelist.html', {'cafelistobj':cafelistobj})

f = open("static/food.csv", 'r')
l = []
lines = f.readlines()
for line in lines:
    l.append(line.split(','))
f.close()

data1 = l[1:44]

api_key = '40124b835a096dbece7e6048d3858777'
def restau_list(request):
    return render(request, 'main/restau_list.html', {'data1':data1, 'api_key':api_key})
#    return render(request, 'main/restau_list.html', {'data':data})g

def restau_list2(request):
    return render(request, 'main/restau_list2.html', {'data1':data1, 'api_key':api_key})
#    return render(request, 'main/restau_list.html', {'data':data})g

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
