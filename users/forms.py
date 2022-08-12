from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from shop.bulma_mixin import BulmaMixin

class SignUpForm(BulmaMixin, UserCreationForm):
    username = forms.CharField(label='Write your username')
    email = forms.EmailField(label='Write your email')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



from django.contrib.auth.forms import AuthenticationForm


class SignInForm(BulmaMixin ,AuthenticationForm):
    
    username = forms.CharField(label='Username')
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'password']




class EditProfileForm(BulmaMixin, forms.ModelForm):
    email = forms.EmailField(label='Write your email')
    first_name = forms.CharField(label='Write your first name')
    last_name = forms.CharField(label='Write your last name')
    username = forms.CharField(label='Write your name')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']


from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(BulmaMixin, PasswordChangeForm):
    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['old_password','new_password1', 'new_password2' ]