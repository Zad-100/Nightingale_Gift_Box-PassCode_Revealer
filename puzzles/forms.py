from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Colour_and_Fashion, FoodTreats, Entertainment, MusicSongs
from .models import PersonalLifestyle, Travel, RelationshipsSentiments


class IsCrosswordSolvedForm(forms.Form):
    """
    Form for validating the successful completion of the crossword puzzle
    by taking a processed string of letters as input.
    """

    # A simply charfield for Nightingale to input the final string of letters
    # after solving the crossword puzzle and following the steps to get the
    # final string of letters.
    final_string = forms.CharField(
        label="Enter Final String",
        widget=forms.TextInput(attrs={
            'placeholder': "ewy",
        }),
    )
# end class IsCrosswordSolvedForm



class PasscodeForm(forms.Form):
    """Form to take passcode from Nightingale for verification of passcode."""

    passcode = forms.IntegerField(
        label="Enter the passcode for verification, here:",
        widget=forms.PasswordInput(attrs={
            'placeholder': "000",
        }),
        validators=[
            MinValueValidator(100, "Passcode is 3-digits only; Try again!"),
            MaxValueValidator(999, "Passcode is 3-digits only; Try again!"),
        ]
    )
# end class PasscodeForm



class OptionalCategoriesForm(forms.Form):
    """Form to take Optional Categories of Nightingale."""
    
    personal_lifestyle = forms.BooleanField(
        label="Personal & Lifestyle (2 Qs)",
        required=False,
    )

    travel = forms.BooleanField(
        label="Travel (2 Qs)",
        required=False,
    )
# end class OptionalCategoriesForm



class ColoursFashionForm(forms.ModelForm):
    """Form to take Colour and Fashion Preferences of Nightingale."""
    # Setting custom labels and any other attributes for the fields
    favourite_general_color = forms.CharField(
        label="What's your go-to color that brightens up any day?",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite General Colour",
        }),
    )

    cute_color = forms.CharField(
        label="There's always that one color that looks super cute. Which is it for you?",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite Cute Colour",
        }),
    )

    worst_general_color = forms.CharField(
        label="What's that colour that always makes you feel like you are having cramps?",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Worst General Colour",
        }),
    )

    favourite_dress_color = forms.CharField(
        label="Every girl has that dress color that makes them feel invincible. What's yours?",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite Dress Colour",
        }),
    )

    favourite_outfit = forms.CharField(
        label="We have already talked about the colour you like your dresses to be, but what's the best outfit of the lot?",
        widget=forms.Textarea(attrs={
            'placeholder': "Your Go-To Outfit",
            'cols': 50, 'rows': 4,
        }),
    )

    favourite_traditional_dress_color = forms.CharField(
        label="When thinking about your favorite traditional attire, which color stands out?",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite Traditional Dress Colour",
        }),
    )

    favourite_cover_shoes_bracelets_color = forms.CharField(
        label="If you were to pick one color for your shoes, bracelets, or covers, what would it be?",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite Accessory/Jewellery Colour",
        }),
    )

    worst_outfit = forms.CharField(
        label="That one outfit that you would never wear even when you are a ghost?",
        widget=forms.Textarea(attrs={
            'placeholder': "Write about the worst outfits",
            'cols': 50, 'rows': 4,
        }),
    )

    favourite_shoe_wear = forms.CharField(
        label="Well well, what would you like your komal komal paon to tread the mighty Earth using?",
        widget=forms.Textarea(attrs={
            'placeholder': "Your Favourite Shoe-Wear",
            'cols': 50, 'rows': 4,
        }),
    )

    worst_shoe_wear = forms.CharField(
        label="What would give your komal feet splinters?",
        widget=forms.Textarea(attrs={
            'placeholder': "The Worst (may be painful) Shoe-Wear",
            'cols': 50, 'rows': 4,
        }),
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = Colour_and_Fashion
        exclude = ['owner']
    # end class Meta
# end class ColoursFashionForm



class FoodTreatsForm(forms.ModelForm):
    """Form to take Food Preferences of Nightingale."""

    favourite_food = forms.CharField(
        label="If some food's the favourite of a foodie, it's got be a serious deal. I wanna know what's yours.",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite Food-Item",
        }),
    )

    worst_food = forms.CharField(
        label="And if a foodie downrates something, it's even a bigger deal. What's that food that you think should be obliterated from the face of the Earth?",
        widget=forms.TextInput(attrs={
            'placeholder': "The Food You Absolutely Hate",
        }),
    )

    favourite_ice_cream_flavour = forms.CharField(
        label="Ice-creams are to our mouth the same as what a golden lit up sunset is to our eyes. Only if, the flavour's right. Your right flavour?",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite Ice-Cream Flavour",
        }),
    )

    worst_ice_cream_flavour = forms.CharField(
        label="Yeah, sunset to our eyes and all too poetic, but what's that flavour that makes you wish all hell to break loose on the inventor?",
        widget=forms.TextInput(attrs={
            'placeholder': "The Absolute Worst Ice-Cream Flavour",
        }),
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = FoodTreats
        exclude = ['owner']
    # end class Meta
# end class FoodTreatsForm



class EntertainmentForm(forms.ModelForm):
    """Form to take Entertainment Preferences of Nightingale."""

    favourite_movie_of_all_time = forms.CharField(
        label="What's that one movie you can just watch on loop like a luniac for the rest of your life?",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite Movie of All Time (Any - Bolly/Holly/Tolly/Kolly/...)",
        }),
    )

    favourite_series_of_all_time = forms.CharField(
        label="This is the series that pops up in your head everytime someone asks - 'What you binging on next?' but some sane voice screams in your head - 'you have watched it like what a zillion times already!'",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite Series of All Time (Any - Bolly/Holly/Tolly/Kolly/...)",
        }),
    )

    favourite_indian_movie_of_all_time = forms.CharField(
        label="Bring that desi in you out. What's THE ONE for you in the world of Indian Films?",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite INDIAN Movie of All Time",
        }),
    )

    favourite_indian_series_of_all_time = forms.CharField(
        label="Don't tell me your fav is 'The Office' and when it comes to Indian Series it's 'The Office'. I mean, you can, but seriously what's the Indian Series you drool on?",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite INDIAN Series of All Time",
        }),
    )

    favourite_book_or_author = forms.CharField(
        label="The bookworm inside you knows what em talking about. What's that book or author that you can't get enough of?",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite Book or Author",
        }),
    )

    favourite_general_genre = forms.CharField(
        label="I know, I know, it's obvious for all those who know you. But you have to tell that genre that you love the most!",
        widget=forms.TextInput(attrs={
            'placeholder': "Your Favourite Gernre (Movies/Books/Series/...)",
        }),
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = Entertainment
        exclude = ['owner']
    # end class Meta
# end class EntertainmentForm



class MusicSongsForm(forms.ModelForm):
    """Form to take Music & Songs Preferences of Nightingale."""

    all_time_favourite_song = forms.CharField(
        label="Umm, em gonna ask you your fav song. But, NO BTS allowed. Just kidding! Not kidding. No seriously, kidding. No, not kidding at all. Mayyyyyyy be kidding.",
        widget=forms.TextInput(attrs={
            'placeholder': "Your All Time Favourite Song (Any - Foreign/Indian)",
        }),
    )

    all_time_favourite_singer = forms.CharField(
        label="I don't wanna give away free points, but I have to ask. Who's your fav singer? But here's the twist: NO JK. Haha kidding!!!! No, ... actually you know the rest.",
        widget=forms.TextInput(attrs={
            'placeholder': "Your All Time Favourite Singer",
        }),
    )

    all_time_favourite_indian_song = forms.CharField(
        label="Which song does the desi inside you love the most?",
        widget=forms.TextInput(attrs={
            'placeholder': "Your All Time Favourite INDIAN Song",
        }),
    )

    all_time_favourite_indian_singer = forms.CharField(
        label="Favourite INDIAN singer? And nhi BTS Indian ARMY mai nhi hai, pagli! * SMH",
        widget=forms.TextInput(attrs={
            'placeholder': "Your All Time Favourite INDIAN Song",
        }),
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = MusicSongs
        exclude = ['owner']
    # end class Meta
# end class MusicSongsForm



class PersonalLifestyleForm(forms.ModelForm):
    """Form to take Personal and Lifestyle Preferences of Nightingale."""

    favourite_past_time = forms.CharField(
        label="Velle time toh baut hain tre paas, I know, but what's that one thing you love doing the most in your free time?",
        widget=forms.Textarea(attrs={
            'placeholder': "Your Favourite Past Time",
            'cols': 50, 'rows': 4,
        }),
    )

    want_to_learn = forms.CharField(
        label="I know you are a genius, I-know-everything-in-this-world and all, but what's that one thing you want to learn still?",
        widget=forms.Textarea(attrs={
            'placeholder': "Whatever You Really Want to Learn",
            'cols': 50, 'rows': 4,
        }),
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = PersonalLifestyle
        exclude = ['owner']
    # end class Meta
# end class PersonalLifestyleForm



class TravelForm(forms.ModelForm):
    """Form to take Travel Dreams of Nightingale."""

    favourite_place = forms.CharField(
        label="Priya = Hamesha ghumi ghumi... So, Ms. Ghummakkadd, what's that one place you HAVE GONE to and just want to go 'mai yehin bass ke mar jaanaa chaahaat hun!!!'?",
        widget=forms.Textarea(attrs={
            'placeholder': "Your Favourite Ghummi-Ghummi Place",
        }),
    )

    dream_destination = forms.CharField(
        label="And what's that one place you have never been to but want to go 'mai wahaan kabhi jaake, bass ke mar jaanaa chaahaati hun!!!'?",
        widget=forms.Textarea(attrs={
            'placeholder': "Your Dream Ghummi-Ghummi Place",
            'cols': 40, 'rows': 3,
        }),
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = Travel
        exclude = ['owner']
    # end class Meta
# end class TravelForm



class RelationshipsSentimentsForm(forms.ModelForm):
    """Form to take Food Preferences of Nightingale."""

    all_time_best_memory = forms.CharField(
        label="What's that memory that is the most frangrant flower in your garden of memories?",
        widget=forms.Textarea(attrs={
            'placeholder': "All Time Best Memory For You",
            'cols': 60, 'rows': 5,
        }),
    )

    all_time_best_memory_with_me = forms.CharField(
        label="And say, you are a bee, then which flower would you be most attracted to in the shared garden of memories between us? Umm... I meant, what's your fav memory with me? 🙂",
        widget=forms.Textarea(attrs={
            'placeholder': "All Time Best Memory For You Of/With Me",
            'cols': 60, 'rows': 5,
        }),
    )

    best_gift_ever_received = forms.CharField(
        label="Of all the gifts you have received, which one is the second most cherished (I know this comes at first, of course)?",
        widget=forms.Textarea(attrs={
            'placeholder': "The Best Gift You Ever Received",
            'cols': 60, 'rows': 5,
        }),
    )

    unforgettable_gesture_from_someone = forms.CharField(
        label="What's something that someone did for you that you can never forget? Like ever? Like ever ever? Like ever ever ever? Like ever ever ever ever? Like ever... You get the idea, right?",
        widget=forms.Textarea(attrs={
            'placeholder': "An Unforgettable Gesture From Someone",
            'cols': 60, 'rows': 5,
        }),
    )

    unforgettable_gesture_from_me = forms.CharField(
        label="This is where I want my compliments for something I did. Haha kidding. Instead, just tell me what I had done that would have gotten me this compliment. 🙈",
        widget=forms.Textarea(attrs={
            'placeholder': "An Unforgettable Gesture From Me",
            'cols': 60, 'rows': 5,
        }),
    )

    value_most_in_relationship = forms.CharField(
        label="Any kind of relationship is beautiful. Relating to people, vibing with them, it's precious. Though, you tell me what you consider the X-factor in any kind of relationship?",
        widget=forms.Textarea(attrs={
            'placeholder': "Thing You Value Most In Any Kind Of Relationship",
            'cols': 60, 'rows': 5,
        }),
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = RelationshipsSentiments
        exclude = ['owner']
    # end class Meta
# end class RelationshipsSentimentsForm