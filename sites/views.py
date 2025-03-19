from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .PostForm import PostForm
from .CommentForm import CommentForm

def home_page(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post.html', {'post': post, 'comments': comments})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_page', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'post': post})