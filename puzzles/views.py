from os import name
from django.shortcuts import render, redirect

from .forms import OptionalCategoriesForm
from .forms import ColoursFashionForm, FoodTreatsForm, EntertainmentForm
from .forms import MusicSongsForm, PersonalLifestyleForm, TravelForm
from .forms import RelationshipsSentimentsForm

# Create your views here.

def index(request):
    """The home page of puzzles"""
    return render(request, 'puzzles/index.html')
# end view index()


def slider_puzzle(request):
    """The slider puzzle page"""
    return render(request, 'puzzles/slider_puzzle.html')
# end view sliderPuzzle()


def crossword_puzzle(request):
    """The crossword puzzle page"""
    return render(request, 'puzzles/crossword_puzzle.html')
# end view crosswordPuzzle()


def dummy_form_main_view(request):
    """
    The dummy form page where Nightingale will select the category of
    questions she wants to answer
    """

    mandatory_categories = {
        "Colours and Fashion": 10,
        "Food and Treats": 4,
        "Entertainment": 6,
        "Music and Songs": 4,
        "Memories": 6,
    }

    optional_categories = {
        "Personal and Lifestyle": 2,
        "Travel": 2,
    }

    if request.method == 'POST':
        form = OptionalCategoriesForm(request.POST)
        if form.is_valid():
            optCat1 = form.cleaned_data['personal_lifestyle']
            optCat2 = form.cleaned_data['travel']

            ## Debug - print the selected categories
            print("optCat1: ", optCat1)
            print("optCat2: ", optCat2)

            # Create a list of categories to be saved in Django's
            # user session
            request.session['selected_categories'] = [
                'colours-fashion',
                'food-treats',
                'entertainment',
                'music-songs',
                'memory-lane',
            ]

            if optCat1:
                request.session['selected_categories'].append(
                    'personal-lifestyle'
                )
            # end if
            if optCat2:
                request.session['selected_categories'].append(
                    'travel'
                )
            # end if
            
            # Also save the index of the current category so that the
            # next category can be fetched
            request.session['curr_category_index'] = 0

            # Redirect to the first category form
            return redirect('puzzles:category-form-view',
                            form_category='colours-fashion')
        # end if
    else:
        form = OptionalCategoriesForm()
    # end if-else

    context = {
        'mandatory_categories': mandatory_categories,
        'optional_categories': optional_categories,
        'form': form,
    }

    return render(request, 'puzzles/dummy_form_main.html', context)
# end view dummy_form_main_view()


def category_form_view(request, form_category):
    """View to render the form for the selected category"""

    Form_Class = None

    # Map form_category to actual form class
    form_map = {
        'colours-fashion': ColoursFashionForm,
        'food-treats': FoodTreatsForm,
        'entertainment': EntertainmentForm,
        'music-songs': MusicSongsForm,
        'personal-lifestyle': PersonalLifestyleForm,
        'travel': TravelForm,
        'memory-lane': RelationshipsSentimentsForm,
    }

    Form_Class = form_map.get(form_category)
    if not Form_Class:
        # Handle error - form type not found
        # Redirect or show an error page
        return redirect('puzzles:dummy-form-main')
    # end if

    if request.method == 'POST':
        form = Form_Class(request.POST)
        if form.is_valid():
            form.save()
            
            # Get the next category
            selected_categories = request.session['selected_categories']
            request.session['curr_category_index'] += 1
            curr_category_index = request.session['curr_category_index']

            if curr_category_index >= len(selected_categories) - 1:
                next_category = selected_categories[curr_category_index]

                # Redirect to the next category form
                return redirect('puzzles:category-form-view',
                                form_category=next_category)
            else:
                # Redirect to message page that will ask her to enter
                # the passcode
                # return redirect('puzzles:passcode-check')
                return redirect('puzzles:index')
            # end if-else
    else:
        form = Form_Class()
    # end if-else

    context = {'form': form}
    return render(request, 'puzzles/category_form.html', context)
# end view dummy_form()


# def passcode_check(request):
#     """Page to check if she's got the passcode right - right digits and order"""
#     return render(request, 'puzzles/passcode_check.html')
# # end view passcode_check()