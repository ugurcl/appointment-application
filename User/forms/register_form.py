from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="Ad",
        widget=forms.TextInput(attrs={
            'placeholder': 'Adınızı girin',
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Soyad",
        widget=forms.TextInput(attrs={
            'placeholder': 'Soyadınızı girin',
        
        })
    )
    email = forms.EmailField(
        required=True,
        label="E-posta",
        widget=forms.EmailInput(attrs={
            'placeholder': 'E-posta adresinizi girin',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Kullanıcı adınızı girin',
            'class': 'form-control'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Şifrenizi girin',
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Şifrenizi tekrar girin',
            'class': 'form-control'
        })
