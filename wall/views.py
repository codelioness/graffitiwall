from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Post

# Create your views here.
def index(request):
    post_list = Post.objects.order_by('-pub_date')[:20]
    context = {'post_list': post_list}
    return render(request, 'wall/index.html', context)

def new_post(request):
    context = {'colors': Post.COLOR_CHOICES}
    return render(request, 'wall/post.html', context)

def posted(request):
    try:
        post = Post(post_text=request.POST['message'], author_name=request.POST['name'], pub_date=timezone.now(), color=request.POST['color'])
    except KeyError:
        return render(request, 'wall/post.html', {'error_message': "You forgot something!"})
    else:
        post.save();
        return HttpResponseRedirect(reverse('wall:index'))