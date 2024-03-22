from django.urls import path
from .views import home,Grafics

urlpatterns = [
    
    path('',home),
    path('grafics/',Grafics),
    
]

