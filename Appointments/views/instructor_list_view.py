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
      search = request.GET.get('search', '').strip()

      if not search:
         users = UserProfile.objects.filter(is_verified=True)
      else:
         search_parts = search.split()
         
         query = Q()

         query |= Q(user__first_name__icontains=search_parts[0]) | \
                  Q(user__last_name__icontains=search_parts[0]) | \
                  Q(bio__icontains=search_parts[0]) 

         for part in search_parts[1:]:
               query &= (
                  Q(user__first_name__icontains=part) |
                  Q(user__last_name__icontains=part) |
                  Q(bio__icontains=part)
               )

         query &= Q(is_verified=True)
         users = UserProfile.objects.filter(query)

      # Kullanıcı verilerini hazırlıyoruz
      content_data = []
      for user in users:
         user_data = {
               "title": user.title.title if user.title and user.title.title else '',
               "first_name": user.user.first_name if user.user and user.user.first_name else '',
               "last_name": user.user.last_name if user.user and user.user.last_name else '',
               'bio': user.bio if user.bio else '',
               'profile_picture': user.profile_picture.url if user.profile_picture else '',
               'contact_email': user.contact_email if user.contact_email else '',
         }
         content_data.append(user_data)

      try:
         return JsonResponse({'data': content_data}, status=200)
      except Exception as e:
         return JsonResponse({'error': str(e)}, status=500)

class SearchInstitution(View):
   def get(self, request, *args, **kwargs):
        value = request.GET.get('value', '').strip()

        if not value:
            data = UserProfile.objects.filter(is_verified=True)
        else:
            data = UserProfile.objects.filter(institution=value, is_verified=True) 
        content_data = [
            {
                "title": _.title.title if _.title and _.title.title else '',
                "first_name": _.user.first_name if _.user and _.user.first_name else '',
                "last_name": _.user.last_name if _.user and _.user.last_name else '',
                'bio': _.bio if _.bio else '',
                'profile_picture': _.profile_picture.url if _.profile_picture else '',
                'contact_email': _.contact_email if _.contact_email else '',
            } for _ in data
        ]

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