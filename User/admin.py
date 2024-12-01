from django.contrib import admin
from .models import UserProfile
from django.utils.html import mark_safe

@admin.register(UserProfile)
class UserProfileAdminModel(admin.ModelAdmin):
    list_display = ('id','user__username','user__first_name','user__last_name','user__email','is_active','is_verified','profile_image_format','profile_bio_format')
    search_fields = ('user__username',)
    list_filter = ('user__username',)
    list_editable = ('is_verified','is_active', )
    readonly_fields = ('slug',)
    
    def profile_bio_format(self, obj):
        if obj.bio:
            return obj.bio if len(obj.bio) < 90 else obj.bio[:90] + '...'
        
    def profile_image_format(self, obj):
        if obj.profile_picture:
            return mark_safe(f'<img src="{obj.profile_picture.url}" width="100" height="100" style="object-fit:cover">')
    profile_image_format.short_description = 'Profil Resmi'
    profile_bio_format.short_description   = 'Biyografı'