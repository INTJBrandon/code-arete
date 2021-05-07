from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from.models import POST
b = 0
e = 4
limit = POST.objects.count()
def home(request):
    
    posts = POST.objects.all()[:3]
    
    context = {
        'post': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

def posts(request):
    b = 0
    e = 4
    posts = POST.objects.all()[b:e]
    
    context = {
        'post' : posts,
        'e' : e,
        'limit' : limit  
    }

    return render(request, 'blog/posts.html', context)

def older(request):
    global b
    global e
    
    if request.method == 'POST':
        if e < limit:   
            b = b + 4
            e = e + 4
        posts = POST.objects.all()[b:e]
        
        context = {
            'post' : posts,
            'b' : b
        }

        return render(request, 'blog/posts.html', context,)
    
def newer(request):
    global b
    global e
    
    if request.method == 'POST':
        if b > 0: 
            b = b - 4
            e = e - 4
        posts = POST.objects.all()[b:e]
        
        context = {
            'post' : posts,
            'e' : e,
            'limit' : limit  
        }

        return render(request, 'blog/posts.html', context)

def post_detail(request, id):
    obj = get_object_or_404(POST, id=id)
    
    context = {
        'obj': obj
    }
    
    return render(request, 'blog/posts_detail.html', context)
    