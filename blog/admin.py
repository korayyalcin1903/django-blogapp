from django.contrib import admin
from django.core import serializers

from blog.models import Blog, Category, Comment, Video


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","get_categories")

    def get_categories(self,obj):
        return ",".join([category.name for category in obj.categories.all()])

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title")
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text",)
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Video)
admin.site.register(Comment,CommentAdmin)

