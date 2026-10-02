from django.contrib import admin
from .models import StudyResource
# Register your models here.

@admin.register(StudyResource)
class StudyResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit', 'category', 'status', 'created_at')
    list_filter = ('category', 'status', 'unit')
    search_fields = ('title', 'description', 'unit__code', 'unit__name')
    list_display_links = ('title',)