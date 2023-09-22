from django import forms
from django.forms import widgets
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        
        fields = ["full_name","email","text",]
        exclude = ['post','date']
        
        widgets = {
            "full_name": widgets.TextInput(attrs={"class":"form-control"}),
            "email": widgets.EmailInput(attrs={"class":"form-control"}),
            "text": widgets.Textarea(attrs={"class":"form-control","rows":"3"}),
        }