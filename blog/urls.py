from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('index', views.index),
    path('blogs', views.blogs, name="blogs"),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("category/<slug:slug>/<slug:child_slug>", views.child_by_category, name="child_by_category"),
    path('blogs/<slug:slug>', views.blog_details, name="blog_details"),
    path('search', views.blog_search, name="blog_search"),
]