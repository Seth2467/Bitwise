from django.shortcuts import render
from .models import Exam
# Create your views here.

def exam_timetable(request):
    exams = Exam.objects.all().order_by(
        'exam_date',
        'start_time',
        'due_date'
    )

    return render (request, 'exams/exam_timetable.html', {
        'exams': exams
    })