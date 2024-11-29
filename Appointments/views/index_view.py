from django.views.generic.base import TemplateView
from django.views.generic import View
from Contact.forms import ContactForm
from django.shortcuts import render, redirect


class IndexView(View):
    template_name = 'app/index.html'
    def get(self, request, *args, **kwargs):
        contact_form = ContactForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form':contact_form
            }
        )