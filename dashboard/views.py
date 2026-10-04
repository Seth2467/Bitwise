from datetime import datetime, timedelta

from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q

from Timetable.models import TimetableEntry
from exams.models import Exam
from .models import EngineeringContent


def dashboard(request):
    now = datetime.now()
    today = now.date()
    today_name = now.strftime('%A')
    current_time = now.time()
    is_weekend = today_name in ['Saturday', 'Sunday']

    if 5 <= now.hour < 12:
        greeting = "Good morning, Engineer"
    elif 12 <= now.hour < 17:
        greeting = "Good afternoon, Engineer"
    elif 17 <= now.hour < 21:
        greeting = "Good evening, Engineer"
    else:
        greeting = "Good night, Engineer"

    engineering_contents = EngineeringContent.objects.filter(
        is_active=True,
        published_at__lte=timezone.now(),
        expires_at__gt=timezone.now()
    ).order_by('-published_at')

    today_classes = TimetableEntry.objects.filter(
        day=today_name,
        bounced=False
    ).order_by('start_time')

    ongoing_class = None
    next_class = None

    for class_entry in today_classes:
        if class_entry.start_time <= current_time <= class_entry.end_time:
            ongoing_class = class_entry
        elif class_entry.start_time > current_time and next_class is None:
            next_class = class_entry

    exam_window_end = today + timedelta(days=2)

    upcoming_exams = Exam.objects.filter(
        is_cancelled=False
    ).filter(
        Q(exam_date__range=(today, exam_window_end)) |
        Q(due_date__range=(today, exam_window_end))
    ).order_by(
        'exam_date',
        'due_date',
        'start_time'
    )

    next_exam = upcoming_exams.first()

    exam_days = None
    exam_label = None

    if next_exam:
        exam_date = next_exam.exam_date or next_exam.due_date

        if exam_date:
            exam_days = (exam_date - today).days

            if exam_days == 0:
                exam_label = "Today"
            elif exam_days == 1:
                exam_label = "Tomorrow"
            elif exam_days == 2:
                exam_label = "In 2 days"

    context = {
        'greeting': greeting,
        'today': today,
        'ongoing_class': ongoing_class,
        'next_class': next_class,
        'next_exam': next_exam,
        'exam_label': exam_label,
        'is_weekend': is_weekend,
        'engineering_contents': engineering_contents,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )