"""Defines the URL patterns for puzzles"""

from django.urls import path

from . import views

app_name = 'puzzles'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Slider Puzzle Page
    path('slider-puzzle/', views.sliderPuzzle, name='sliderPuzzle'),

    # Crossword Puzzle Page
    path('crossword-puzzle/', views.crosswordPuzzle, name='crosswordPuzzle'),

    
]