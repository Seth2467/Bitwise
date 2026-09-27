from django.shortcuts import render
from .models import TimetableEntry
# Create your views here.
def timetable(request):
    entries = TimetableEntry.objects.all().order_by('day','start_time')

    return render(request, 'timetable/timetable.html', {'entries': entries})
