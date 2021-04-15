from django.urls import path
from .models import Avalanche_Accident

from . import views


urlpatterns = [
    path('', views.ListAvalanche_Accident.as_view()),
    path('<int:pk>/', views.DetailAvalanche_Accident.as_view()),
]