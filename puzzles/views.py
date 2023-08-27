from django.shortcuts import render, redirect

from .forms import OptionalCategoriesForm
from .forms import ColoursFashionForm, FoodTreatsForm, EntertainmentForm
from .forms import MusicSongsForm, PersonalLifestyleForm, TravelForm
from .forms import RelationshipsSentimentsForm
from .forms import PasscodeForm

PASSCODE = 123

# Create your views here.

def index(request):
    """The home page of puzzles"""
    return render(request, 'puzzles/index.html')
# end view index()



# ***********Slider Puzzle and its Message Page Views***********
def slider_puzzle(request):
    """The slider puzzle page"""
    return render(request, 'puzzles/slider_puzzle.html')
# end view slider_puzzle()


def message_1(request):
    """The message page after completing slider puzzle successfully"""
    return render(request, 'puzzles/message_1.html')
# end view message_1()



# ***********Crossword Puzzle and its Message Pages Views***********
def crossword_puzzle(request):
    """The crossword puzzle page"""
    return render(request, 'puzzles/crossword_puzzle.html')
# end view crossword_puzzle()


def message_2(request):
    """The message page after completing crossword puzzle successfully"""
    return render(request, 'puzzles/message_2.html')
# end view message_2()



# ***********Counterfiet Form abd its Message Page Views***********
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
            selected_categories = request.session.get('selected_categories', [])
            request.session['curr_category_index'] += 1
            curr_category_index = request.session.get('curr_category_index', 0)

            if curr_category_index <= len(selected_categories) - 1:
                next_category = selected_categories[curr_category_index]

                # Redirect to the next category form
                return redirect('puzzles:category-form-view',
                                form_category=next_category)
            else:
                # All categories submitted by Nightingale; so clear
                # session variables
                del request.session['selected_categories']
                del request.session['curr_category_index']

                # Redirect to third message page
                return redirect('puzzles:message-3')
            # end if-else
    else:
        form = Form_Class()
    # end if-else

    context = {'form': form}
    return render(request, 'puzzles/category_form.html', context)
# end view dummy_form()


def message_3(request):
    """The message page after completing the dummy form successfully"""
    return render(request, 'puzzles/message_3.html')
# end view message_3()



# ***********Passcode Check and Final Message Page Views***********
def passcode_check(request):
    """Page to check if she's got the passcode right - right digits and order"""

    # Session variable storing the total number of attempts left
    if 'attempts_left' not in request.session:
        request.session['attempts_left'] = 3
    # end if

    # Session variable to store whether to show the wait and redirect script
    if 'show_redirect_script' not in request.session:
        request.session['show_redirect_script'] = False
    # end if

    if request.method == 'POST':
        form = PasscodeForm(request.POST)
        if form.is_valid():
            passcode = form.cleaned_data['passcode']

            print("")
            print("")
            print("******************PASSCODE********************", passcode,
                  sep='\n')
            print("")
            print("")

            if passcode == PASSCODE:
                # Reset the number of attempts for another attempt
                del request.session['attempts_left']

                # Change the session state of verification to True
                request.session['passcode_verified'] = True
                # Show the wait and redirect script
                request.session['show_redirect_script'] = True
            else:
                # Decrement the attempts left
                request.session['attempts_left'] -= 1

                if request.session['attempts_left'] <= 0:
                    # Reset the number of attempts for another attempt
                    del request.session['attempts_left']
                    
                    # Change the session state of verification to False
                    request.session['passcode_verified'] = False
                    # Show the wait and redirect script
                    request.session['show_redirect_script'] = True
                # end if
            # end if-else
    else:
        form = PasscodeForm()
    # end if-else

    context = {
        'form': form,
        'attempts_left': request.session.get('attempts_left', 3),
        'passcode_verified': request.session.get('passcode_verified', None),
        'show_redirect_script': request.session.get('show_redirect_script',
                                                    False),
    }

    return render(request, 'puzzles/passcode_check.html', context)
# end view passcode_check()


# The very final page of the entire web app!!!
def final_message(request):
    """The final message page"""
    return render(request, 'puzzles/final_message.html')
# end view final_message()