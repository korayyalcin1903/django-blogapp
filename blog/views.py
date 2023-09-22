from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import CommentForm
from blog.models import Blog, Category, Comment, Video


@login_required(login_url="account/login")
def index(request):
    blog = Blog.objects.filter(is_home = True, is_active = True).order_by('date')
    lastets_comments = Comment.objects.order_by("-date")[:3]
    context = {
        "blogs": blog[:6],
        "categories": Category.objects.all(),
        "videos": Video.objects.all(), 
        "lastets_comments":lastets_comments
    }
    
    return render(request, "blog/index.html", context)

@login_required(login_url="account/login")
def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active = True),
        "categories": Category.objects.all(),
        "videos": Video.objects.all()
    }
    
    return render(request,"blog/blogs.html", context)

def blogs_by_category(request, slug):
    selected_category = get_object_or_404(Category, slug=slug)

    subcategories = Category.objects.filter(parent=selected_category)

    blogs = Blog.objects.filter(categories__in=[selected_category] + list(subcategories), is_active=True)

    context = {
        "blogs": blogs,
        "categories": Category.objects.all(),
        "selected_category": selected_category.slug,
        "videos": Video.objects.all() 
    }
    
    return render(request, "blog/blogs.html", context)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    categories = Category.objects.all()
    comment_form = CommentForm()
    latests_blog = Blog.objects.order_by("-date")[:3]
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = blog
            comment.save()
            return HttpResponseRedirect(reverse("blog_details", args=[slug]))
    else:
        comment_form = CommentForm()
    
    return render(request, "blog/blog-details.html", {
        "blog":blog,
        "categories":categories,
        "comments": blog.comments.all(),
        "comment_form":comment_form,
        "videos": Video.objects.all(),
        "lastest_blogs": latests_blog
    })

def child_by_category(request,slug,child_slug):
    selected_category = get_object_or_404(Category, slug=child_slug)
    selected_parent = get_object_or_404(Category, slug=child_slug).parent

    subcategories = Category.objects.filter(parent=selected_category)

    blogs = Blog.objects.filter(categories__in=[selected_category] + list(subcategories), is_active=True)

    context = {
        "blogs": blogs,
        "categories": Category.objects.all(),
        "selected_category": selected_category.parent,
        "selected_parent": selected_parent.slug,
        "videos": Video.objects.all() 
    }
    
    print(context.get("selected_parent"))
    
    return render(request, "blog/blogs.html", context)

def blog_search(request):
    if 'q' in request.GET and request.GET.get('q'):
        q = request.GET['q']
        blogs = Blog.objects.filter(title__contains=q)
    else:
        blogs = Blog.objects.all()
    
    context = {
        "blogs":blogs,
        "videos": Video.objects.all(), 
    }
    
    return render(request, "blog/search.html", context)
