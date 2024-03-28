from django.urls import path
from workouts.views import index, exercise_details

urlpatterns = [
    path('', index, name='index'),
    path('exercise-details/', exercise_details, name='exercise_details'),
]

