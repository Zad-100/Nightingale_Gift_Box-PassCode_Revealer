from django.db import models

# Create your models here.

# 1. Required
class Colour_and_Fashion(models.Model):
    """Model representing Colour and Fashion Preferences of Nightingale."""
    favourite_general_color = models.CharField(max_length=200)
    worst_general_color = models.CharField(max_length=200)
    cute_color = models.CharField(max_length=200)
    favourite_dress_color = models.CharField(max_length=200)
    favourite_traditional_dress_color = models.CharField(max_length=200)
    favourite_cover_shoes_bracelets_color = models.CharField(max_length=200)
    favourite_outfit = models.TextField()
    worst_outfit = models.TextField()
    favourite_shoe_wear = models.TextField()
    worst_shoe_wear = models.TextField()
# end class Colour_and_Fashion


# 2. Required
class FoodTreats(models.Model):
    """Model representing Food and Treats Preferences of Nightingale."""
    favourite_food = models.CharField(max_length=200)
    worst_food = models.CharField(max_length=200)
    favourite_ice_cream_flavour = models.CharField(max_length=200)
    worst_ice_cream_flavour = models.CharField(max_length=200)
# end class FoodTreats


# 3. Required
class Entertainment(models.Model):
    """Model representing Entertainment Preferences of Nightingale."""
    favourite_movie_of_all_time = models.CharField(max_length=400)
    favourite_series_of_all_time = models.CharField(max_length=400)
    favourite_indian_movie_of_all_time = models.CharField(max_length=400)
    favourite_indian_series_of_all_time = models.CharField(max_length=400)
    favourite_book_or_author = models.CharField(max_length=400)
    favourite_general_genre = models.CharField(max_length=400)
# end class Entertainment


# 4. Required
class MusicSongs(models.Model):
    """Model representing Music and Songs Preferences of Nightingale."""
    all_time_favourite_song = models.CharField(max_length=400)
    all_time_favourite_singer = models.CharField(max_length=400)
    all_time_favourite_indian_song = models.CharField(max_length=400)
    all_time_favourite_indian_singer = models.CharField(max_length=400)
# end class MusicSongs


# 5. Not Required
class PersonalLifestyle(models.Model):
    """Model representing Personal Lifestyle Preferences of Nightingale."""
    favourite_past_time = models.TextField()
    want_to_learn = models.TextField()
# end class PersonalLifestyle


# 6. Not Required
class Travel(models.Model):
    """Model representing Travel Preferences of Nightingale."""
    favourite_place = models.CharField(max_length=200)
    dream_destination = models.TextField(null=True)
# end class Travel


# 7. Required
class RelationshipsSentiments(models.Model):
    """Model representing Relationships and Sentiments of Nightingale."""
    all_time_best_memory = models.TextField()
    all_time_best_memory_with_me = models.TextField()
    best_gift_ever_received = models.TextField()
    unforgettable_gesture_from_someone = models.TextField()
    unforgettable_gesture_from_me = models.TextField()
    value_most_in_relationship = models.TextField()
# end class RelationshipsSentiments