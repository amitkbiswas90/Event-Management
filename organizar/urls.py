from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-event/', views.create_event, name='create-event'),
    path('create-participant/', views.create_participant, name='create-participant'),
    path('create-category/', views.create_category, name='create-category'),
    path('organizer-dashboard/', views.organizer_dashboard, name='organizer-dashboard'),  
    path('update-event/<int:id>/',views.update_event, name='update-event'),
    path('delete-event/<int:id>/',views.delete_event, name='delete-event'),
    path('view-event/',views.view_event, name='view-event'),

]
