# blog/views.py
from django.shortcuts import render, redirect , get_object_or_404
from .models import Post , Comment
from django.http import HttpResponse
from django.utils import timezone 
from django.contrib.auth.decorators import login_required
from .forms import PostForm , CommentForm

CATEGORY_CHOICES = [
    ("tech", "Tech"),
    ("sports", "Sports"),
    ("entertainment", "Entertainment"),
    ("politics", "Politics"),
    ("fashion", "Fashion"),
    ("food", "Food"),
    ("travel", "Travel"),
    ("other", "Other"),
]

def post_list(request):
    orderby=request.GET.get('OrderBy')
    
    if orderby=="p_a":
        posts = Post.objects.all().order_by('-published_at')

    else:
        posts = Post.objects.all()

    search=request.GET.get('search')
    if search and orderby=="p_a":
        posts = Post.objects.filter(title__icontains=search).order_by('-published_at')
    
    cat = request.GET.get('category')
    
    if cat and orderby=="p_a":
        posts = Post.objects.filter(category=cat).order_by('-published_at')
        
    
    if search:
        posts = Post.objects.filter(title__icontains=search)
    
    
    if cat:
        posts = Post.objects.filter(category=cat)

    comments=Comment.objects.all().order_by('-created_at')[:5]
    
    return render(request, 'blog/post_list.html', {'posts': posts , 'categories': CATEGORY_CHOICES , 'comments' : comments})

@login_required
def add_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'blog/add_post.html', {'form': form})

    if request.method == 'POST':
        request_post = request.POST.copy()
        request_post.update({"user": request.user.id})
        form = PostForm(request_post, request.FILES )
        if form.is_valid():
            post = form.save(commit=False)
            post.published_at = timezone.now()
            post.user = request.user
            post.save()
            return redirect('/')
        else:
            print(form.errors)

    # If the request method is neither GET nor POST or the user is not authenticated
    return HttpResponse("You are not authorized to view this page", status=401)


def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:view_post', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/view_post.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST' and request.user.is_authenticated and request.user == post.user:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.image = request.FILES['image']
            print(post.image) 
            form.save()
            return redirect('blog:view_post', post_id=post.id)
    else:
        return HttpResponse("You are not authorized to view this page" , status=401)

    return render(request, 'blog/update_post.html', {'form': form})