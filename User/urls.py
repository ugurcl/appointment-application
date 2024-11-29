from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    RegisterView,
    ProfileView
)
from .send_mail import activate_account


urlpatterns = [
    path(route='giris-yap/', view=LoginView.as_view(),name='login'),
    path(route='cikis-yap', view=LogoutView.as_view(), name='logout'),
    path("kayit-ol/", RegisterView.as_view(), name="register"),
    path("activate/<uidb64>/<token>/", activate_account, name="activate"),
    path(route='profil/', view=ProfileView.as_view(), name='profile')
]
