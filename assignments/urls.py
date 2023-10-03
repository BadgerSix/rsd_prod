from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main, name='assignments_main'),
    path('details/<int:id>', views.details, name='assignment_details'),
    path('delete/<int:id>', views.delete, name='assignment_delete'),
]