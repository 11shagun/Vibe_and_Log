from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.filter(published = True)
    return render(request, "Vibe_and_Log/home.html", {"posts":posts})

def post_details(request, slug):
    post = get_object_or_404(Post, slug = slug, published = True)
    return render(request, "Vibe_and_Log/post_details.html", {"post":post})