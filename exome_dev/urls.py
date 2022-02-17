from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('families/', views.families, name='families'),
    path('family/<family_id>/', views.family, name='family'),
    path('patient/<id>/', views.patient, name='patient')
]