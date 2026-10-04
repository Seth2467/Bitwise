from django.contrib import admin
from .models import EngineeringContent


@admin.register(EngineeringContent)
class EngineeringContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_at', 'expires_at', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'content')