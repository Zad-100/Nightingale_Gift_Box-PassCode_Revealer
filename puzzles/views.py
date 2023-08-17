from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page of puzzles"""
    return render(request, 'puzzles/index.html')
# end view index()