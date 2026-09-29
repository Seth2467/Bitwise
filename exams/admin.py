from django.contrib import admin
from .models import Exam
# Register your models here.

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):

    list_display = (
        'unit',
        'exam_type',
        'mode',
        'exam_date',
        'start_time',
        'end_time',
        'due_date',
        'is_cancelled',
    ) 

    list_filter = (
        'exam_type',
        'mode',
        'is_cancelled',
    )

    search_fields = (
        'unit__code',
        'unit__name',
    )