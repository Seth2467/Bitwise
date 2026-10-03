from datetime import datetime, time, timedelta

from django.shortcuts import render
from django.utils import timezone

from .models import Exam


def exam_timetable(request):

    now = timezone.localtime(timezone.now())
    today = now.date()

    exams = Exam.objects.all()

    upcoming_exams = []

    for exam in exams:

        if exam.mode == "Take-away":

            if not exam.due_date:

                if not exam.is_cancelled:
                    exam.schedule_date = None
                    upcoming_exams.append(exam)

                continue

            expiry_time = timezone.make_aware(
                datetime.combine(
                    exam.due_date + timedelta(days=1),
                    time.min
                )
            )

            if exam.is_cancelled:

                if now < expiry_time:
                    exam.schedule_date = exam.due_date
                    upcoming_exams.append(exam)

            else:

                if now < expiry_time:
                    exam.schedule_date = exam.due_date
                    upcoming_exams.append(exam)

        else:

            if not exam.exam_date:

                if not exam.is_cancelled:
                    exam.schedule_date = None
                    upcoming_exams.append(exam)

                continue

            if exam.end_time:

                exam_end = timezone.make_aware(
                    datetime.combine(
                        exam.exam_date,
                        exam.end_time
                    )
                )

            else:

                exam_end = timezone.make_aware(
                    datetime.combine(
                        exam.exam_date + timedelta(days=1),
                        time.min
                    )
                )

            if exam.is_cancelled:

                cancellation_expiry = exam_end + timedelta(hours=3)

                if now < cancellation_expiry:
                    exam.schedule_date = exam.exam_date
                    upcoming_exams.append(exam)

            else:

                if now < exam_end:
                    exam.schedule_date = exam.exam_date
                    upcoming_exams.append(exam)

    upcoming_exams.sort(
        key=lambda exam: (
            exam.schedule_date or today,
            exam.start_time or time.min
        )
    )

    return render(
        request,
        'exams/exam_timetable.html',
        {
            'exams': upcoming_exams,
            'today': today,
        }
    )

def exam_history(request):

    now = timezone.localtime(timezone.now())

    exams = Exam.objects.all()

    completed_exams = []

    for exam in exams:

        if exam.mode == "Take-away":

            if exam.due_date:

                expiry_time = timezone.make_aware(
                    datetime.combine(
                        exam.due_date + timedelta(days=1),
                        time.min
                    )
                )

                if now >= expiry_time:
                    exam.schedule_date = exam.due_date
                    completed_exams.append(exam)

        else:

            if exam.exam_date:

                if exam.end_time:

                    exam_end = timezone.make_aware(
                        datetime.combine(
                            exam.exam_date,
                            exam.end_time
                        )
                    )

                else:

                    exam_end = timezone.make_aware(
                        datetime.combine(
                            exam.exam_date + timedelta(days=1),
                            time.min
                        )
                    )

                if now >= exam_end:
                    exam.schedule_date = exam.exam_date
                    completed_exams.append(exam)

    completed_exams.sort(
        key=lambda exam: (
            exam.schedule_date or now.date(),
            exam.start_time or time.min
        ),
        reverse=True
    )

    return render(
        request,
        'exams/exam_history.html',
        {
            'exams': completed_exams,
            'today': now.date(),
        }
    )