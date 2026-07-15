from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=True)

    cat_name = kwargs.get('cat_name')
    if cat_name:
        posts = posts.filter(category__name=cat_name)

    author_username = kwargs.get('author_username')
    if author_username:
        posts = posts.filter(author__username=author_username)

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts, pk = pid)
    context = {"post" : post}
    return render(request, 'blog/blog-single.html', context)

def test(request):
    return render(request,"test.html")

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=True)
    posts = posts.filter(category__name=cat_name)
    context = {'posts' : posts}
    return render(request, "blog/blog-home.html", context)

def search_view(request):
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
       if s := request.GET.get('s'):
           posts = posts.filter(content__icontains=s)
    
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)