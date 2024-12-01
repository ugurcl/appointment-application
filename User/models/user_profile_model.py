from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models
import random

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',verbose_name="Kullanıcı", error_messages={'unique':'Kullanıcı adı sistemde kayıtlı'})
    bio = models.TextField(verbose_name='Kullanıcı Biyografisi',max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(verbose_name='Kullanıcı Profil Resmi',upload_to='profile_pictures/', blank=True, null=True, default='defaults/logo.jpg')
    is_verified = models.BooleanField(default=False, verbose_name="Kullanıcı yetkili mi ?")  
    is_active = models.BooleanField(default=False, verbose_name='Kullanıcı aktif mi ?')
    slug = models.SlugField(unique=True, blank=True) 
    contact_email = models.EmailField(verbose_name='Kullanıcıların size ulaşabileceği e-posta adresi', unique=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_value = f'{self.user.first_name}-{self.user.last_name}-{(random.randint(1,99999))}'
            self.slug = slugify(slug_value.replace('ı','i'))
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'user_profile'
        managed = True
        verbose_name = 'profil'
        verbose_name_plural = 'Kullanıcı Profilleri'