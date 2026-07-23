from django import template
from blog.models import Post
from blog.models import Category, Comments
register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status = True).count()
    return posts

@register.simple_tag(name='post')
def function():
    posts = Post.objects.filter(status = True)
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    return Comments.objects.filter(post=pid, approved=True).count()

@register.filter
def snippet(valve):
    return valve[:50]

@register.inclusion_tag('blog/popularposts.html')
def latestposts():
    posts = Post.objects.filter(status = True).order_by('published_date')[:1]
    return {'posts' :posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()

    cat_dict = {}

    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()

    return {'categories': cat_dict}