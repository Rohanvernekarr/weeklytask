from django.shortcuts import render
from django.http import Http404

# Create your views here.

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

TASK= {
    'monday' : 'Plan the weekend ahead',
    'tuesday' : 'Prepare for meetings', 
    'wednesday' : 'Grocery shopping',
    'thursday' : 'Workout session',
    'friday' : 'Clean the house',
    'saturday' : 'Family movie night',
    'sunday' : 'Gardening and relaxation'
}

def index(request):
    context = {'days': DAYS}
    return render(request, 'index.html', context)

def day_task(request, day):
    day = day.lower()
    if day not in DAYS:
        raise Http404("Day not found")
    task = TASK.get(day, "No task assigned for this day.")
    context = {
        'day': day.capitalize(),
        'task': task
    }
    return render(request, 'day.html', context)