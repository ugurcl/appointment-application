from django.urls import path
from .views import IndexView, InstructorListView,LoadMoreContentView,SearchInstitution,Search


urlpatterns = [
    path(route='', view=IndexView.as_view(), name='index'),
    path(route='ögretim-görevlileri/', view=InstructorListView.as_view(), name='instructor_list'),
    path(route='ogretim-gorevlileri/daha-fazla-yukle/', view=LoadMoreContentView.as_view(), name='load_more'),
     path(route='ogretim-gorevlileri/kurum-arama/', view=SearchInstitution.as_view(), name='search_institution'),
      path(route='ogretim-gorevlileri/arama/', view=Search.as_view(), name='search')
]
