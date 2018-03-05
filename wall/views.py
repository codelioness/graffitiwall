from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.
def index(request):
    post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'post_list': post_list,}
    return render(request, 'wall/index.html', context)

def new_post(request):
    return HttpResponse("This is the post page!")

def posted(request):
    return HttpResponse("Posted!")