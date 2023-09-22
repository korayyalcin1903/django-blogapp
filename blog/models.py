from datetime import datetime
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
        
class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField()
    image = models.ImageField(upload_to="blogs")
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    date = models.DateTimeField(default=datetime.now, null=False, blank=True, editable=False)
    categories = models.ManyToManyField(Category, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.slug
        
class Video(models.Model):
    title = models.CharField(max_length=150)
    video_link = models.URLField()
    blog = models.ManyToManyField(Blog, null=True, blank=True)
    level = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    full_name = models.CharField(max_length=100,default="")
    email = models.EmailField(default="")
    text = models.TextField(max_length=150)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)
