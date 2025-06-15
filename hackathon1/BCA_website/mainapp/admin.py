from django.contrib import admin
from .models import Semester, Subject, Notice

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester')
    list_filter = ('semester',)
    search_fields = ('name',)

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'notice_type', 'date', 'semester')
    list_filter = ('notice_type', 'semester')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
