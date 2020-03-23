from django.shortcuts import render,redirect
from .models import Articles
from django.contrib.auth.decorators import login_required
from . import forms
#from django.http import HttpResponse

# Create your views here.
def articles_list(request):
  articles= Articles.objects.all().order_by('date')
  return render(request,'articles/articles_list.html', {'articles':articles})


def articles_details(request,slug):
  #return HttpResponse(slug)
  articles=Articles.objects.get(slug=slug)
  return render(request,'articles/articles_details.html',{'articles':articles})

@login_required(login_url="/accounts/login")
def article_create(request):
  if request.method=="POST":
    form=forms.CreateArticles(request.POST, request.FILES)
    if form.is_valid():
      #save article to db
      istance=form.save(commit=False)
      istance.author=request.user
      istance.save()
      return redirect('articles:list')
  else:
    form=forms.CreateArticles()
  return render(request,'articles/article_create.html', {'form':form})