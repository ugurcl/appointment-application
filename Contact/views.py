from django.shortcuts import render, redirect
from .models import ContactModel
from django.views.generic import View
from .forms import ContactForm
from django.contrib import messages
from Appointments.models import AppointmentCreation

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        try:
            ip = x_forwarded_for.split(',')[0].split()
        except ValueError:
            ip = '0.0.0.0'
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ' '.join(ip) or '0.0.0.0'

class ContactViews(View):
    template_name = 'app/contact.html'
   
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        _ = AppointmentCreation.objects.first().staff_member.bio
        print(_)
        return render(
            request=request,
            template_name=self.template_name,
            context={'form': form}
        )
    def post(self, request, *args, **kwargs):
        referer = request.META.get('HTTP_REFERER', '/')
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.user = request.user
            
            post.ip_address = get_client_ip(request=request)
            post.save()
            messages.success(
                request=request,
                message='Mesajınız başarıyla iletildi'
            )
            return redirect(referer)
        else:
            messages.error(request=request, message='Mesajınız iletilemedi! Lütfen tekrar deneyin')
        form = ContactForm(request.POST)
        return render(
            request=request,
            template_name=self.template_name,
            context={'form':form}
        )