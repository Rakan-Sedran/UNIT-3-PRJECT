from django.contrib import admin
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_important', 'start_date', 'end_date', 'created_at')
    list_filter = ('category', 'is_important')
    search_fields = ('title', 'content')
