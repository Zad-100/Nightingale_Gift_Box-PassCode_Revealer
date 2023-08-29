"""
Contains instructions specific to each category of the counterfeit form.
There are presently 7 Categories: Colours and Fashion, Food and Treats,
Entertainment, Music and Songs, Memories, Personal and Lifestyle, Travel.
Each category has a set of instructions that are displayed to Nightingale when
she comes across that particular form. The said instructions would be saved as
a dictionary with the category name as the key and the instructions as the
value. This would be imported in the views.py file and passed as a part of the
context dictionary to the category_form template.
"""

# # ***********Colours and Fashion***********
colours_and_fashion_instruct = """
The very first of the categories is Colours and Fashion. This would be all \
about the colours of your life. And of course, fashion and colours go \
hand-in-hand. So, let's get started with the \
questions! 😌
(Also, a short wish: Yehi prarthanaa rahegi ki yeh Birthday and \
in the years to come, tri life mai colours he colours hon 🌈 and, of course, \
tre pasand ke colours nhi milenge hameshaa, but jab jab naa hon, mujhe yaad \
krnaa; I shall try my best ki unn colours pe primer lagaake waapass tre fav \
colours se paint kr dun! 🎨🖌😉)
"""

# # ***********Food and Treats***********
food_and_treats_instruct = """
This part is all about your absolute favourite!!! Food 😏 A cute foodie like \
you needs to be heard of her likes and dislikes! Toh chaliye suru krte hain \
binaa cooking time waste kiye! 😋
"""

# # ***********Entertainment***********
entertainment_instruct = """
Well well, ab itnaa binge krti reheti hai, toh obviously entertainment \
ke baare form bantaa thaa. May be yeh form more weightage de tre overall \
score ko... I dunno, em just saying. 🤷‍♀️ Ready steady pooooooo! 🏁
"""

# # ***********Music and Songs***********
music_and_songs_instruct = """
Hoping that your life also grooves like your favourite tracks forever, 🎶 \
and you flow with the rhythm of life, let's see how you do in this section. \
🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵 Don't forget to whistle or hum \
that song while you are answering. 🌚
"""

# # ***********Memories***********
memories_instruct = """
I cherish my memories more than I cherish anything else in my life. And I \
like to think everybody does too. So, let's see how much you remember about \
the most bitter sweet moments of your life. 🤔 (Also, a small wish part 2: \
I hope that in the future when someone asks you about some of your beautiful \
moments in life, this app features in that list. 🤞🙈😊)
"""

# # ***********Personal and Lifestyle***********
personal_and_lifestyle_instruct = """
"Saale personal kyaa ho rhaa hai beee??? Bhapp!! 😒" - Praying that this \
isn't your reaction to this form. 🙏😂 But for the sake of the game, \
come on! 🌚
"""

# # ***********Travel***********
travel_instruct = """
I know how much you like to travel, and thus this section. 🌍🌎🌏 \
Ab bataao apne kuch travel dreams ke baare, and let's see how much you know \
the inner traveller in you. 😏
"""

# # ***********Instructions Dictionary***********
instructions_map = {
    "colours-fashion": colours_and_fashion_instruct,
    "food-treats": food_and_treats_instruct,
    "entertainment": entertainment_instruct,
    "music-songs": music_and_songs_instruct,
    "memory-lane": memories_instruct,
    "personal-lifestyle": personal_and_lifestyle_instruct,
    "travel": travel_instruct,
}