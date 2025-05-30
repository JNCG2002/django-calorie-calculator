from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/<int:calculation_id>/', views.result, name='result'),
    path('about/', views.about, name='about'),
]