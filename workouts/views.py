from django.shortcuts import render, get_object_or_404
from workouts.models import Exercise

def index(request):
    return render(request, 'Gym/index.html')

def exercise_details(request,):
    exercises = Exercise.objects.all()
    return render(request, 'Gym/exercise_details.html', {'exercise_info': exercises})