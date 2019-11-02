from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponse
import datetime as dt 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def welcome(request):
    date = dt.date.today()
    new = NeighbourHood.objects.all()
    return render(request, 'welcome.html', {"date": date, "new": new})
    
def create_hood(request):
    if request.method == 'POST':
        form = NeighborForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user
            hood.save()
            return redirect('welcome')
    else:
        form = NeighborForm()
    return render(request, 'hood.html', {'form': form})
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('new-post')

    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            bus = form.save(commit=False)
            bus.user = current_user
            bus.save()
        return redirect('new-business')

    else:
        form = BusinessForm()
    return render(request, 'new_business.html', {"form": form})


def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.neighbourhood = neighbourhood
    request.user.save()
    return redirect('hood')


def leave_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.neighbourhood = None
    request.user.save()
    return redirect('hood')


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