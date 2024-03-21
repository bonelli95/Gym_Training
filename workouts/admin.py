from django.contrib import admin
from workouts.models import Exercise

class listExercises(admin.ModelAdmin):
    list_display = ('id', 'title', 'title2')
    list_display_links = ('id', 'title', 'title2')
    search_fields = ('title', 'title2',)
admin.site.register(Exercise, listExercises)