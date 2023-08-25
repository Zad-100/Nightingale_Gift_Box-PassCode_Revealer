# Generated by Django 4.2.4 on 2023-08-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entertainment',
            old_name='favouriteBollywoodMovieOfAllTime',
            new_name='favourite_book_or_author',
        ),
        migrations.RenameField(
            model_name='entertainment',
            old_name='favouriteBollywoodSeriesOfAllTime',
            new_name='favourite_general_genre',
        ),
        migrations.RenameField(
            model_name='entertainment',
            old_name='favouriteBookOrAuthor',
            new_name='favourite_indian_movie_of_all_time',
        ),
        migrations.RenameField(
            model_name='entertainment',
            old_name='favouriteGeneralGenre',
            new_name='favourite_indian_series_of_all_time',
        ),
        migrations.RenameField(
            model_name='entertainment',
            old_name='favouriteMovieOfAllTime',
            new_name='favourite_movie_of_all_time',
        ),
        migrations.RenameField(
            model_name='entertainment',
            old_name='favouriteSeriesOfAllTime',
            new_name='favourite_series_of_all_time',
        ),
        migrations.RenameField(
            model_name='foodtreats',
            old_name='favouriteFood',
            new_name='favourite_food',
        ),
        migrations.RenameField(
            model_name='foodtreats',
            old_name='favouriteIceCreamFlavour',
            new_name='favourite_iceCream_flavour',
        ),
        migrations.RenameField(
            model_name='foodtreats',
            old_name='worstFood',
            new_name='worst_food',
        ),
        migrations.RenameField(
            model_name='foodtreats',
            old_name='worstIceCreamFlavour',
            new_name='worst_icecream_flavour',
        ),
        migrations.RenameField(
            model_name='musicsongs',
            old_name='allTimeFavouriteBollywoodSinger',
            new_name='all_time_favourite_indian_singer',
        ),
        migrations.RenameField(
            model_name='musicsongs',
            old_name='allTimeFavouriteBollywoodSong',
            new_name='all_time_favourite_indian_song',
        ),
        migrations.RenameField(
            model_name='musicsongs',
            old_name='allTimeFavouriteSinger',
            new_name='all_time_favourite_singer',
        ),
        migrations.RenameField(
            model_name='musicsongs',
            old_name='allTimeFavouriteSong',
            new_name='all_time_favourite_song',
        ),
        migrations.RenameField(
            model_name='personallifestyle',
            old_name='favouritePasttime',
            new_name='favourite_pasttime',
        ),
        migrations.RenameField(
            model_name='personallifestyle',
            old_name='wantToLearn',
            new_name='want_to_learn',
        ),
        migrations.RenameField(
            model_name='relationshipssentiments',
            old_name='allTimeBestMemory',
            new_name='all_time_best_memory',
        ),
        migrations.RenameField(
            model_name='relationshipssentiments',
            old_name='allTimeBestMemoryWithMe',
            new_name='all_time_best_memory_with_me',
        ),
        migrations.RenameField(
            model_name='relationshipssentiments',
            old_name='bestGiftEverReceived',
            new_name='best_gift_ever_received',
        ),
        migrations.RenameField(
            model_name='relationshipssentiments',
            old_name='mostCherishedGiftFromMe',
            new_name='unforgettable_gesture_from_me',
        ),
        migrations.RenameField(
            model_name='relationshipssentiments',
            old_name='unforgettableGestureFromMe',
            new_name='unforgettable_gesture_from_someone',
        ),
        migrations.RenameField(
            model_name='relationshipssentiments',
            old_name='unforgettableGestureFromSomeone',
            new_name='value_most_in_relationship',
        ),
        migrations.RenameField(
            model_name='travel',
            old_name='dreamDestination',
            new_name='favourite_place',
        ),
        migrations.RemoveField(
            model_name='musicsongs',
            name='favouriteGenre',
        ),
        migrations.RemoveField(
            model_name='personallifestyle',
            name='catOrDog',
        ),
        migrations.RemoveField(
            model_name='relationshipssentiments',
            name='valueMostInRelationship',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='favouritePlace',
        ),
        migrations.AddField(
            model_name='travel',
            name='dream_destination',
            field=models.TextField(null=True),
        ),
    ]
