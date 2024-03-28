from django.shortcuts import render, redirect
from workouts.models import Exercise
from django.contrib import messages

def index(request):
    return render(request, 'Gym/index.html')

def exercise_details(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Please log in to access this page.')
        return redirect('login')
     
    training_type = request.GET.get('type')
    if training_type:
        exercises = Exercise.objects.filter(training_type=training_type)
    else:
        exercises = Exercise.objects.all()
    return render(request, 'Gym/exercise_details.html', {'exercise_info': exercises})
