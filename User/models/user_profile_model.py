from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',verbose_name="Kullanıcı")
    bio = models.TextField(verbose_name='Kullanıcı Biyografisi',max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(verbose_name='Kullanıcı Profil Resmi',upload_to='profile_pictures/', blank=True, null=True, default='defaults/logo.jpg')
    is_verified = models.BooleanField(default=False, verbose_name="Kullanıcı yetkili mi ?")  
    is_active = models.BooleanField(default=False, verbose_name='Kullanıcı aktif mi ?')
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'user_profile'
        managed = True
        verbose_name = 'profil'
        verbose_name_plural = 'Kullanıcı Profilleri'