from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Post


# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['urllink']:
            post = Post()
            post.title = request.POST['title']

            # does the url begin with 'https://' or http:// #REQUIRED TO DIRECTED TO INPUT URL
            if request.POST['urllink'].startswith('https://') or request.POST['urllink'].startswith('http://'):
                post.url = request.POST['urllink']
            else:
                post.url = 'http://' + request.POST['urllink']

            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('index')

        else:
            return render(request, 'posts/create.html', {'error': 'Tiles and/or Url is missing'})

    else:
        return render(request, 'posts/create.html')


def index(request):
    post = Post.objects.order_by('-votes_total')
    return render(request, 'posts/index.html', {'posts': post})

def upvote(request,pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total += 1
        post.save()
        return redirect('index')

def downvote(request,pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total -= 1
        post.save()
        return redirect('index')


