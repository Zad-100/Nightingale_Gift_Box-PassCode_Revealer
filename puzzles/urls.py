"""Defines the URL patterns for puzzles"""

from django.urls import path

from . import views

app_name = 'puzzles'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Slider Puzzle Page
    path('slider-puzzle/', views.slider_puzzle, name='slider-puzzle'),

    # Crossword Puzzle Page
    path('crossword-puzzle/', views.crossword_puzzle, name='crossword-puzzle'),

    # Dummy Form Page
    
    # Page to select the form category
    path('how-much-do-you-know-yourself/', views.dummy_form_main_view,
        name='dummy-form-main'),
    
    # Form page for the selected category
    path('how-much-do-you-know-yourself/<str:form_category>/',
        views.category_form_view, name='category-form-view'),
]