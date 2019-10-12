from django.shortcuts import render
from .models import Post

# to import http response 
#from django.http import HttpResponse


# Create your views here.

#def home(request):
 #   return HttpResponse('<doctype>...')

""" posts = [
    {
        'author':'Nitika',
        'title':'Blog Post 1',
        'content': 'First Post Content',
        'date_posted':'October 10 2019'
    },
    {
        'author':'AK',
        'title':'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted':'October 11 2019'
    }
] """


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html',{'title': 'About'})

#def about(request):
#    return HttpResponse('<h1>Blog About</h1>')
