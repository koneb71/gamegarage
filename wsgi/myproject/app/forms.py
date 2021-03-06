from django import forms
from .models import User, Category, Game_info

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'contact_number']

        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
        }

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class AddGameForm(forms.ModelForm):
    class Meta:
        model = Game_info
        fields = ['title', 'description', 'platform']

class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['old_password', 'password', 'confirm_password']

        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'old_password': forms.PasswordInput(),
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }