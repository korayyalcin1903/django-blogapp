from .models import Profile
import random
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control form-control-user","placeholder":"Enter Email Address..."}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control password","placeholder":"Enter Password"}))
    remember_me = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={"class":"custom-control-input"}))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            self.add_error("email","Email is not found")
        
        return email
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email","first_name","last_name")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Enter Password"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Enter Re-Password"})
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Enter First Name"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Enter Last Name"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control form-control-user","placeholder":"Enter Email Address..."})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control form-control-user","placeholder":"Enter Email Address..."})

        self.fields["email"].required = True
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error("error","This email is used")
        return email
    
    def save(self,commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get("password1"))
        user.username = "{}_{}_{}".format(
            self.cleaned_data.get("first_name").replace("ç","c").replace("ö","o").replace("ü","u").replace("ı","i").replace("ğ","g").replace("ş","s").lower(),
            self.cleaned_data.get("last_name").replace("ç","c").replace("ö","o").replace("ü","u").replace("ı","i").replace("ğ","g").replace("ş","s").lower(),
            random.randint(11111,99999)
        )
        
        if commit:
            user.save()

        return user
    
class UserForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email","avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget = forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"})
        self.fields["last_name"].widget = forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"})
        self.fields["email"].widget = forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
        self.fields["avatar"].widget = forms.EmailInput(attrs={"class": "form-control", "type": "file"})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("avatar",)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["avatar"].widget = forms.FileInput(attrs={"class":"form-control","type":"file"})
        
class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})