from django.shortcuts import render
from workouts.models import Exercise

def index(request):
    return render(request, 'Gym/index.html')

def exercise_details(request,):
    training_type = request.GET.get('type')
    if training_type:
        exercises = Exercise.objects.filter(training_type=training_type)
    else:
        exercises = Exercise.objects.all()
    return render(request, 'Gym/exercise_details.html', {'exercise_info': exercises})