from django.shortcuts import render
from .models import TimetableEntry
from datetime import datetime

# Create your views here.
def timetable(request):

    today = datetime.now().strftime('%A')
    current_time = datetime.now().time()

    day_order = {
        'Monday': 1,
        'Tuesday':2,
        'Wednesday':3,
        'Thursday':4,
        'Friday':5,
    }
    entries = TimetableEntry.objects.all()

    for entry in entries:
        if entry.bounced:
            entry.status = 'Bounced'
        
        elif entry.day != today:
            entry.status = ''
        elif current_time < entry.start_time:
            entry.status = 'Upcoming'
        elif current_time >= entry.end_time:
            entry.status = 'Finished'
        else:
            entry.status = 'Ongoing'
    entries = sorted(
        entries,
        key= lambda entry:(
            day_order[entry.day], 
            entry.start_time
        )
    )

    return render(request, 'timetable/timetable.html', {'entries': entries, 'today': today})
