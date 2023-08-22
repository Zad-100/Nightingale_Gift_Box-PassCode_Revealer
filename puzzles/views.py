from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page of puzzles"""
    return render(request, 'puzzles/index.html')
# end view index()

def sliderPuzzle(request):
    """The slider puzzle page"""
    return render(request, 'puzzles/sliderPuzzle.html')
# end view sliderPuzzle()

def crosswordPuzzle(request):
    """The crossword puzzle page"""
    return render(request, 'puzzles/crosswordPuzzle.html')
# end view crosswordPuzzle()

def hangmanPuzzle(request):
    """The hangman puzzle page"""
    return render(request, 'puzzles/hangmanPuzzle.html')