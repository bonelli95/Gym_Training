from django.urls import path
from workouts.views import index, exercise_details
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('exercise-details/', exercise_details, name='exercise_details'),
]

