from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

class ProfileView(LoginRequiredMixin,View):
    login_url = '/kullanici/giris-yap'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):
        return render(
            request=request,
            template_name='users/profile.html'
        )
    def post(self, request, *args, **kwargs):
        ... 