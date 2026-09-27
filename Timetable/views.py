from django.shortcuts import render
from .models import TimetableEntry
# Create your views here.
def timetable(request):

    day_order = {
        'Monday': 1,
        'Tuesday':2,
        'Wednesday':3,
        'Thursday':4,
        'Friday':5,
    }
    entries = TimetableEntry.objects.all()
    entries = sorted(
        entries,
        key= lambda entry:(
            day_order[entry.day], 
            entry.start_time
        )
    )

    return render(request, 'timetable/timetable.html', {'entries': entries})
