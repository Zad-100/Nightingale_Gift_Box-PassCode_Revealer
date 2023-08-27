"""Defines the URL patterns for puzzles"""

from django.urls import path

from . import views

app_name = 'puzzles'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Slider Puzzle Page
    path('slider-puzzle/', views.slider_puzzle, name='slider-puzzle'),

    # Message 1 Page
    path('message-1/', views.message_1, name='message-1'),

    # Crossword Puzzle Page
    path('crossword-puzzle/', views.crossword_puzzle, name='crossword-puzzle'),

    # Message 2 Page
    path('message-2/', views.message_2, name='message-2'),

    # Dummy Form Page
    # Page to select the form category
    path('how-much-do-you-know-yourself/', views.dummy_form_main_view,
        name='dummy-form-main'),
    
    # Form page for the selected category
    path('how-much-do-you-know-yourself/<str:form_category>/',
        views.category_form_view, name='category-form-view'),

    # Message 3 Page
    path('message-3/', views.message_3, name='message-3'),

    # Page to verify the correct passcode
    path('passcode-check/', views.passcode_check, name='passcode-check'),

    # Page to display final message
    path('final-message/', views.final_message, name='final-message'),
]