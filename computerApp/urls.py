from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('machines/',
     views.machine_list_view,
      name='machines'),
    path('machine/<pk>',
      views.machine_detail_view,
      name='machine-detail'),
    
    path('personnels/',
    views.personnel_list_view,
     name='personnels'),
    
    path('personnel/<pk>',
    views.personnel_detail_view,
      name='personnel-detail'),

    
]