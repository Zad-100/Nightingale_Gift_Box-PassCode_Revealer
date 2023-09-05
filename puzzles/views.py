from django.shortcuts import render, redirect

from .forms import OptionalCategoriesForm
from .forms import ColoursFashionForm, FoodTreatsForm, EntertainmentForm
from .forms import MusicSongsForm, PersonalLifestyleForm, TravelForm
from .forms import RelationshipsSentimentsForm
from .forms import PasscodeForm, IsCrosswordSolvedForm
from .category_instructions import instructions_map



PASSCODE = 314
FIRST_DIGIT = str(PASSCODE)[0]
SECOND_DIGIT = str(PASSCODE)[1]
THIRD_DIGIT = str(PASSCODE)[2]

FINAL_STRING = sorted("HURATEY".lower())
FINAL_STRING_LIST = list(FINAL_STRING)



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

    context = {'message_1_digit': SECOND_DIGIT}

    return render(request, 'puzzles/message_1.html', context)
# end view message_1()



# ***********Crossword Puzzle and its Message Pages Views***********
def crossword_puzzle(request):
    """The crossword puzzle page"""

    return render(request, 'puzzles/crossword_puzzle.html')
# end view crossword_puzzle()


def crossword_puzzle_check(request):
    """The page to verify if crossword puzzle solved correctly"""

    isSolved = -1 # -1: not checked, 0: not solved, 1: solved

    if request.method == 'POST':
        form = IsCrosswordSolvedForm(request.POST)
        if form.is_valid():
            final_string = form.cleaned_data['final_string']

            print("")
            print("")
            print("******************FINAL STRING********************",
                  final_string, sep='\n')
            print("")
            print("")

            if list(sorted(final_string.lower())) == FINAL_STRING_LIST:
                isSolved = 1
            else:
                isSolved = 0
            # end if

            print("")
            print("***********************************************************")
            print("isSolved: ", isSolved)
            print("***********************************************************")
            print("")
        # end if
    else:
        form = IsCrosswordSolvedForm()
    # end if-else

    context = {
        'form': form,
        'isSolved': isSolved,
    }

    return render(request, 'puzzles/crossword_puzzle_check.html', context)
# end view crossword_puzzle_check()


def message_2(request):
    """The message page after completing crossword puzzle successfully"""
    
    context = {'message_2_digit': FIRST_DIGIT}

    return render(request, 'puzzles/message_2.html', context)
# end view message_2()



# ***********Counterfiet Form abd its Message Page Views***********
def dummy_form_main_view(request):
    """
    The dummy form page where Nightingale will select the category of
    questions she wants to answer
    """

    mandatory_categories = {
        "Colours & Fashion": 10,
        "Food & Treats": 4,
        "Entertainment": 6,
        "Music & Songs": 4,
        "Memories": 6,
    }

    # optional_categories = {
    #     "Personal & Lifestyle": 2,
    #     "Travel": 2,
    # }

    if request.method == 'POST':
        form = OptionalCategoriesForm(request.POST)
        if form.is_valid():
            optCat1 = form.cleaned_data['personal_lifestyle']
            optCat2 = form.cleaned_data['travel']

            ## Debug - print the selected categories
            print("")
            print("***********************************************************")
            print("optCat1: ", optCat1)
            print("optCat2: ", optCat2)
            print("***********************************************************")
            print("")

            # Create a list of categories to be saved in Django's
            # user session
            if 'selected_categories' not in request.session:
                request.session['selected_categories'] = [
                    'colours-fashion',
                    'food-treats',
                    'entertainment',
                    'music-songs',
                    'memory-lane',
                ]
            # end if

            print("")
            print("***********************************************************")
            print("Initialisation request.session['selected_categories']:",
                  request.session['selected_categories'])
            print("***********************************************************")
            print("")

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
            print("")
            print("***********************************************************")
            print("Final request.session['selected_categories']:",
                  request.session['selected_categories'])
            print("***********************************************************")
            print("")
            
            # Also save the index of the current category so that the
            # next category can be fetched
            if 'curr_category_index' not in request.session:
                request.session['curr_category_index'] = 0
            # end if
            print("")
            print("***********************************************************")
            print("Initialisation of request.session['curr_category_index']:",
                  request.session['curr_category_index'])
            print("***********************************************************")
            print("")

            # Redirect to the first category form
            return redirect('puzzles:category-form-view',
                            form_category='colours-fashion')
        # end if
    else:
        form = OptionalCategoriesForm()
    # end if-else

    context = {
        'mandatory_categories': mandatory_categories,
        'form': form,
    }

    print("")
    print("======================START CATEGORIES=============================")
    print("")

    return render(request, 'puzzles/dummy_form_main.html', context)
# end view dummy_form_main_view()


def category_form_view(request, form_category):
    """View to render the form for the selected category"""
    
    print("")
    print("*******************************************************************")
    print("Selected Categories Check:",
          request.session['selected_categories'])
    print("*******************************************************************")
    print("")
    
    Form_Class = None

    # Map form_category to actual form class
    form_map = {
        'colours-fashion': (ColoursFashionForm, "Colours and Fashion"),
        'food-treats': (FoodTreatsForm, "Food and Treats"),
        'entertainment': (EntertainmentForm, "Entertainment"),
        'music-songs': (MusicSongsForm, "Music and Songs"),
        'personal-lifestyle': (PersonalLifestyleForm, "Personal and Lifestyle"),
        'travel': (TravelForm, "Travel"),
        'memory-lane': (RelationshipsSentimentsForm, "Memories"),
    }

    Form_Class = form_map.get(form_category, None)[0]
    category_instruct = instructions_map.get(form_category, None)
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
            curr_category_index = request.session.get('curr_category_index', None)
            print("")
            print("***********************************************************")
            print("Present curr_category_index:", curr_category_index)
            curr_category_index += 1
            print("Incremented curr_category_index (getting next category):", 
                  curr_category_index)
            print("***********************************************************")
            print("")

            if curr_category_index <= len(selected_categories) - 1:
                print("")
                print("*******************************************************")
                print("curr_category_index <= len(selected_categories) - 1",
                      "... still categories left")
                print("*******************************************************")
                print("")
                next_category = selected_categories[curr_category_index]
                request.session['curr_category_index'] = curr_category_index
                print("")
                print("*******************************************************")
                print("Check if curr_category_index updated in session:",
                      request.session['curr_category_index'])
                print("*******************************************************")
                print("")

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
        # end if
    else:
        form = Form_Class()
    # end if-else

    category_name = form_map.get(form_category, None)[1]
    context = {
        'form': form,
        'category_name': category_name,
        'category_instruct': category_instruct,
    }
    return render(request, 'puzzles/category_form.html', context)
# end view dummy_form()


def message_3(request):
    """The message page after completing the dummy form successfully"""

    context = {'message_3_digit': THIRD_DIGIT}

    return render(request, 'puzzles/message_3.html', context)
# end view message_3()



# ***********Passcode Check and Final Message Page Views***********
def passcode_check(request):
    """Page to check if she's got the passcode right - right digits and order"""

    # Session variable storing the total number of attempts left
    if 'attempts_left' not in request.session:
        request.session['attempts_left'] = 3
    # end if

    print("")
    print("*******************************************************************")
    print("Initialisation of request.session['attempts_left']:",
          request.session['attempts_left'])
    print("*******************************************************************")
    print("")

    # Session variable to store whether to show the wait and redirect script
    if 'show_redirect_script' not in request.session:
        request.session['show_redirect_script'] = False
    # end if

    print("")
    print("*******************************************************************")
    print("Initialisation of request.session['show_redirect_script']:",
          request.session['show_redirect_script'])
    print("*******************************************************************")
    print("")

    # Session variable to store whether the passcode is verified
    # passcode_verified = None => initialisation of the page
    # passcode_verified = -1 => wrong passcode entered and there's still
    # attempts left
    # passcode_verified = 0 => attempts are over and still incorrect
    # passcode_verified = 1 => correct passscode entered within attempts
    if 'passcode_verified' not in request.session:
        request.session['passcode_verified'] = None
    # end if

    print("")
    print("*******************************************************************")
    print("Initialisation of request.session['passcode_verified']:",
          request.session['passcode_verified'])
    print("*******************************************************************")
    print("")
    

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

                # Correct passcode entered; passcode_verification = 1
                # Change the session state of verification to 1
                request.session['passcode_verified'] = 1

                print("")
                print("*******************************************************")
                print("Check if passcode_verified updated in session:",
                        request.session['passcode_verified'])
                print("*******************************************************")
                print("")
                
                # Show the wait and redirect script
                request.session['show_redirect_script'] = True

                print("")
                print("*******************************************************")
                print("Check if show_redirect_script updated in session:",
                        request.session['show_redirect_script'])
                print("*******************************************************")
                print("")
            else:
                # Incorrect passcode entered and attempts left;
                # passcode_verification = -1
                # Change the session state of verification to -1
                request.session['passcode_verified'] = -1

                # Decrement the attempts left
                request.session['attempts_left'] -= 1

                print("")
                print("*******************************************************")
                print("Check if attempts_left updated in session:",
                        request.session['attempts_left'])
                print("*******************************************************")
                print("")

                if request.session['attempts_left'] <= 0:
                    # Reset the number of attempts for another attempt
                    del request.session['attempts_left']
                    
                    # Attempts over and still incorrect; passcode_verified = 0
                    # Change the session state of verification to 0
                    request.session['passcode_verified'] = 0

                    print("")
                    print("***************************************************")
                    print("Check if passcode_verified updated in session:",
                            request.session['passcode_verified'])
                    print("***************************************************")
                    print("")

                    # Show the wait and redirect script
                    request.session['show_redirect_script'] = True

                    print("")
                    print("***************************************************")
                    print("Check if show_redirect_script updated in session:",
                            request.session['show_redirect_script'])
                    print("***************************************************")
                    print("")
                # end if
            # end if-else
        # end if
    else:
        form = PasscodeForm()
    # end if-else

    context = {
        'form': form,
        'attempts_left': request.session.get('attempts_left', 3),
        'passcode_verified': request.session.get('passcode_verified', None),
        'show_redirect_script': request.session.get('show_redirect_script',
                                                    False),
        'passcode': str(PASSCODE),
    }

    return render(request, 'puzzles/passcode_check.html', context)
# end view passcode_check()


# The very final page of the entire web app!!!
def final_message(request):
    """The final message page"""

    return render(request, 'puzzles/final_message.html')
# end view final_message()