from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponse
import datetime as dt 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def welcome(request):
    new = NeighbourHood.objects.all()
    return render(request, 'welcome.html', { "new": new})

def hoods(request):
     new = NeighbourHood.objects.all()
     newpost = Post.objects.all()
     business = Business.objects.all()
     return render(request, 'all.html', {"new": new, "newpost":newpost, "business":business})  

@login_required(login_url='/accounts/login')
def hood_details(request,neighbour_id):
     details=NeighbourHood.get_specific_hood(neighbour_id)

     return render(request,'all.html',{"details":details})
@login_required(login_url='/accounts/login')
def bus_details(request,business_id):
     details1=Business.get_specific_bus(business_id)

     return render(request,'new_business.html',{"details1":details1})
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
    newpost = Post.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('hood')

    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form, "newpost": newpost})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form1 = BusinessForm(request.POST, request.FILES)
        if form1.is_valid():
            bus = form1.save(commit=False)
            bus.user = current_user
            bus.save()
        return redirect('hood')

    else:
        form1 = BusinessForm()
    return render(request, 'new_business.html', {"form1": form1})


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

@login_required(login_url='/accounts/login/')     
def add_comment(request,post_id):
    current_user=request.user
    if request.method=='POST':
        image_item=Post.objects.filter(id=post_id).first()

    
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.posted_by=current_user
            comment.comment_image=image_item
            comment.save()
        return redirect('hood')
    else:
        form=CommentForm()
    return render(request,'comment.html',{"form":form,"post_id":post_id})
