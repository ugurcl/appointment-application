from django.urls import path
from .views import IndexView

urlpatterns = [
    path(route='hakkimizda/', view=IndexView.as_view(), name='about')
]
