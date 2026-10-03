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

        if entry.day != today:
            entry.status = ''

        elif current_time >= entry.end_time:

            elapsed_seconds = (
                datetime.combine(datetime.today(), current_time)
                - datetime.combine(datetime.today(), entry.end_time)
            ).total_seconds()

            if elapsed_seconds <= 3600:
                entry.status = 'Finished'
            else:
                entry.status = ''

        elif entry.bounced:
            entry.status = 'Bounced'

        elif current_time < entry.start_time:
            entry.status = 'Upcoming'

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
