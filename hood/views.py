from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def welcome(request):
    date = dt.date.today()
    new = NeighbourHood.objects.all()
    return render(request, 'welcome.html', {"date": date, "new": new})

@login_required(login_url='/accounts/login/')
def profile(request, username=None):
	'''
	Method that fetches a users profile page
	'''
	current_user = request.user
	pi_images = NeighbourHood.objects.filter(user=current_user)

	return render(request,"profile.html",locals(),{"pi_images":pi_images})

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user=request.user
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('profile')
    else:
        form=ProfileForm()
    return render(request,'profile_edit.html',{"form":form})