from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('delete-course/<course_id>/', views.delete_course, name='delete-course'),
    path('delete-flashcard/<flashcard_id>/', views.delete_flashcard, name='delete-flashcard'),
    path('create-deck/', views.create_deck, name='create-deck'),
    path('edit-deck/<deck_id>/', views.edit_deck, name='edit-deck'),
    path('delete-deck/<deck_id>/', views.delete_deck, name='delete-deck'),
    path('study/<study_id>/', views.study, name='study'),
]
