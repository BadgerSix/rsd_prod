from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main, name='members_main'),
    path('details/<int:id>', views.details, name='members_details')
]