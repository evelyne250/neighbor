from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt 
from .models import *

def welcome(request):
    date = dt.date.today()
    new = NeighbourHood.objects.all()
    return render(request, 'welcome.html', {"date": date, "new": new})