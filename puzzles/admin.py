from django.contrib import admin

from .models import Colour_and_Fashion, FoodTreats, Entertainment, MusicSongs
from .models import PersonalLifestyle, Travel, RelationshipsSentiments

# Register your models here.
admin.site.register(Colour_and_Fashion)
admin.site.register(FoodTreats)
admin.site.register(Entertainment)
admin.site.register(MusicSongs)
admin.site.register(PersonalLifestyle)
admin.site.register(Travel)
admin.site.register(RelationshipsSentiments)
