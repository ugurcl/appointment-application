from django.views.generic import View
from User.models import UserProfile, Institution
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import JsonResponse
from User.models import UserProfile
from django.urls import reverse

class Search(View):
   def get(self, request, *args, **kwargs):
      search = request.GET.get('search','')
      if search:
         search_parts = search.split()
         query =  \
            Q(user__first_name__icontains=search_parts[0]) | \
            Q(user__last_name__icontains=search_parts[0]) | \
            Q(bio__icontains=search_parts[0])

         for part in search_parts[1:]:
            query &= (
                  Q(user__first_name__icontains=part) |
                  Q(user__last_name__icontains=part) |
                  Q(bio__icontains=part)
            )
    
         users = UserProfile.objects.filter(query)
      else:
         users = UserProfile.objects.all()

      content_data = [
            {
               "title": _.title.title if _.title.title else '',
               "first_name": _.user.first_name if _.user.first_name else '',
               "last_name": _.user.last_name if _.user.last_name else '',
               'bio': _.bio if _.bio else '',
               'profile_picture': _.profile_picture.url if _.profile_picture else '',
               'contact_email': _.contact_email if _.contact_email else '',


            } for _ in users]
      print(content_data)
      return JsonResponse({'data': content_data})
   

class SearchInstitution(View):
   def get(self, request, *args, **kwargs):
      value = request.GET.get('value','') 
      if value != '':
         data = UserProfile.objects.filter(institution=value)
      else:
         data = UserProfile.objects.all()
      content_data = [
            {
               "title": _.title.title if _.title.title else '',
               "first_name": _.user.first_name if _.user.first_name else '',
               "last_name": _.user.last_name if _.user.last_name else '',
               'bio': _.bio if _.bio else '',
               'profile_picture': _.profile_picture.url if _.profile_picture else '',
               'contact_email': _.contact_email if _.contact_email else '',


            } for _ in data]

      return JsonResponse({'data': content_data})
      
      
   

class LoadMoreContentView(View):
    def get(self, request, *args, **kwargs):
        
      offset = int(request.GET.get('offset', 10))
      limit = 10
      content = UserProfile.objects.filter(is_verified=True, is_active=True)[offset:offset+limit]
      
      content_data = [
            {
               "title": _.title.title if _.title.title else '',
               "first_name": _.user.first_name if _.user.first_name else '',
               "last_name": _.user.last_name if _.user.last_name else '',
               'bio': _.bio if _.bio else '',
               'profile_picture': _.profile_picture.url if _.profile_picture else '',
               'contact_email': _.contact_email if _.contact_email else '',


            } for _ in content]
       
      return JsonResponse({'content':content_data})
    
class InstructorListView(LoginRequiredMixin,View):
   login_url = '/kullanici/giris-yap/'
   def get(self, request, *args, **kwargs):
      users = UserProfile.objects.filter(is_active=True,is_verified=True)[:10]
      institution_list = Institution.objects.all()
      return render(
         request=request,
         template_name='appointment/profile-appointment.html',
         context={'users':users, 'institution_list':institution_list}
      )