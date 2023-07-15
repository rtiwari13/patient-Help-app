from django.urls import path 
from django.conf import settings
from .views import *


urlpatterns = [
    path('', home, name='home'),
     path('',PatientDetails.as_view()),
    
]