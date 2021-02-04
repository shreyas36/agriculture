from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crops/', views.CropListView.as_view(), name='crops'),
    path('crops/entry/', views.CropCreateView.as_view(), name='crops-entry'),
    path('crops/entry/added', views.added, name='added'),
    path('about/', views.about, name='about'),
    path('crops/rice', views.rice, name='rice_data'),
]
