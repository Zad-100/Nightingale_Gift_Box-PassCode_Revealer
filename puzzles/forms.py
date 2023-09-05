from django import forms
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
        label="Input Final String",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
# end class IsCrosswordSolvedForm



class PasscodeForm(forms.Form):
    """Form to take passcode from Nightingale for verification of passcode."""

    passcode = forms.IntegerField(
        label="Enter the passcode for verification, here:",
        widget=forms.PasswordInput()
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
    )

    cute_color = forms.CharField(
        label="There's always that one color that looks super cute. Which is it for you?",
    )

    worst_general_color = forms.CharField(
        label="What's that colour that always makes you feel like you are having cramps?",
    )

    favourite_dress_color = forms.CharField(
        label="Every girl has that dress color that makes them feel invincible. What's yours?",
    )

    favourite_outfit = forms.CharField(
        label="We have already talked about the colour you like your dresses to be, but what's the best outfit of the lot?",
        widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 4}),
    )

    favourite_traditional_dress_color = forms.CharField(
        label="When thinking about your favorite traditional attire, which color stands out?",
    )

    favourite_cover_shoes_bracelets_color = forms.CharField(
        label="If you were to pick one color for your shoes, bracelets, or covers, what would it be?",
    )

    worst_outfit = forms.CharField(
        label="That one outfit that you would never wear even when you are a ghost?",
        widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 4}),
    )

    favourite_shoe_wear = forms.CharField(
        label="Well well, what would you like your komal komal paon to tread the mighty Earth using?",
        widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 4}),
    )

    worst_shoe_wear = forms.CharField(
        label="What would give your komal feet splinters?",
        widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 4}),
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = Colour_and_Fashion
        fields = '__all__'
    # end class Meta
# end class ColoursFashionForm



class FoodTreatsForm(forms.ModelForm):
    """Form to take Food Preferences of Nightingale."""

    favourite_food = forms.CharField(
        label="If some food's the favourite of a foodie, it's got be a serious deal. I wanna know what's yours.",
    )

    worst_food = forms.CharField(
        label="And if a foodie downrates something, it's even a bigger deal. What's that food that you think should be obliterated from the face of the Earth?",
    )

    favourite_ice_cream_flavour = forms.CharField(
        label="Ice-creams are to our mouth the same as what a golden lit up sunset is to our eyes. Only if, the flavour's right. Your right flavour?",
    )

    worst_ice_cream_flavour = forms.CharField(
        label="Yeah, sunset to our eyes and all too poetic, but what's that flavour that makes you wish all hell to break loose on the inventor?",
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = FoodTreats
        fields = '__all__'
    # end class Meta
# end class FoodTreatsForm



class EntertainmentForm(forms.ModelForm):
    """Form to take Entertainment Preferences of Nightingale."""

    favourite_movie_of_all_time = forms.CharField(
        label="What's that one movie you can just watch on loop like a luniac for the rest of your life?",
    )

    favourite_series_of_all_time = forms.CharField(
        label="This is the series that pops up in your head everytime someone asks - 'What you binging on next?' but some sane voice screams in your head - 'you have watched it like what a zillion times already!'",
    )

    favourite_indian_movie_of_all_time = forms.CharField(
        label="Bring that desi in you out. What's THE ONE for you in the world of Indian Films?",
    )

    favourite_indian_series_of_all_time = forms.CharField(
        label="Don't tell me your fav is 'The Office' and when it comes to Indian Series it's 'The Office'. I mean, you can, but seriously what's the Indian Series you drool on?",
    )

    favourite_book_or_author = forms.CharField(
        label="The bookworm inside you knows what em talking about. What's that book or author that you can't get enough of?",
    )

    favourite_general_genre = forms.CharField(
        label="I know, I know, it's obvious for all those who know you. But you have to tell that genre that you love the most!",
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = Entertainment
        fields = '__all__'
    # end class Meta
# end class EntertainmentForm



class MusicSongsForm(forms.ModelForm):
    """Form to take Music & Songs Preferences of Nightingale."""

    all_time_favourite_song = forms.CharField(
        label="Umm, em gonna ask you your fav song. But, NO BTS allowed. Just kidding! Not kidding. No seriously, kidding. No, not kidding at all. Mayyyyyyy be kidding.",
    )

    all_time_favourite_singer = forms.CharField(
        label="I don't wanna give away free points, but I have to ask. Who's your fav singer? But here's the twist: NO JK. Haha kidding!!!! No, ... actually you know the rest.",
    )

    all_time_favourite_indian_song = forms.CharField(
        label="Which song does the desi inside you love the most?",
    )

    all_time_favourite_indian_singer = forms.CharField(
        label="Favourite INDIAN singer? And nhi BTS Indian ARMY mai nhi hai, pagli! * SMH",
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = MusicSongs
        fields = '__all__'
    # end class Meta
# end class MusicSongsForm



class PersonalLifestyleForm(forms.ModelForm):
    """Form to take Personal and Lifestyle Preferences of Nightingale."""

    favourite_past_time = forms.CharField(
        label="Velle time toh baut hain tre paas, I know, but what's that one thing you love doing the most in your free time?",
        widget=forms.Textarea(attrs={'cols': 50, 'rows': 4}),
    )

    want_to_learn = forms.CharField(
        label="I know you are a genius, I-know-everything-in-this-world and all, but what's that one thing you want to learn still?",
        widget=forms.Textarea(attrs={'cols': 50, 'rows': 4}),
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = PersonalLifestyle
        fields = '__all__'
    # end class Meta
# end class PersonalLifestyleForm



class TravelForm(forms.ModelForm):
    """Form to take Travel Dreams of Nightingale."""

    favourite_place = forms.CharField(
        label="Priya = Hamesha ghumi ghumi... So, Ms. Ghummakkadd, what's that one place you have gone to and just want to go 'mai yehin bass ke mar jaanaa chaahaat hun!!!'?",
    )

    dream_destination = forms.CharField(
        label="And what's that one place you have never been to but want to go 'mai wahaan kabhi jaake, bass ke mar jaanaa chaahaati hun!!!'?",
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 3}),
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = Travel
        fields = '__all__'
    # end class Meta
# end class TravelForm



class RelationshipsSentimentsForm(forms.ModelForm):
    """Form to take Food Preferences of Nightingale."""

    all_time_best_memory = forms.CharField(
        label="What's that memory that is the most frangrant flower in your garden of memories?",
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}),
    )

    all_time_best_memory_with_me = forms.CharField(
        label="And say, you are a bee, then which flower would you be most attracted to in the shared garden of memories between us? Umm... I meant, what's your fav memory with me? 🙂",
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}),
    )

    best_gift_ever_received = forms.CharField(
        label="Of all the gifts you have received, which one is the second most cherished (I know this comes at first, of course)?",
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}),
    )

    unforgettable_gesture_from_someone = forms.CharField(
        label="What's something that someone did for you that you can never forget? Like ever? Like ever ever? Like ever ever ever? Like ever ever ever ever? Like ever... You get the idea, right?",
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}),
    )

    unforgettable_gesture_from_me = forms.CharField(
        label="This is where I want my compliments for something I did. Haha kidding. Instead, just tell me what I had done that would have gotten me this compliment. 🙈",
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}),
    )

    value_most_in_relationship = forms.CharField(
        label="Any kind of relationship is beautiful. Relating to people, vibing with them, it's precious. Though, you tell me what you consider the X-factor in any kind of relationship?",
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}),
    )


    class Meta:
        """Meta class to specify model and fields to be used."""
        model = RelationshipsSentiments
        fields = '__all__'
    # end class Meta
# end class RelationshipsSentimentsForm