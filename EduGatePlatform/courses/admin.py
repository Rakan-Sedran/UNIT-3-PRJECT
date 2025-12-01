from django.contrib import admin
from .models import SchoolClass, Subject, ClassSubject, StudentClassEnrollment

# Register your models here.

@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade_level', 'created_at')
    list_filter = ('grade_level',)
    search_fields = ('name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(ClassSubject)
class ClassSubjectAdmin(admin.ModelAdmin):
    list_display = ('school_class', 'subject', 'teacher', 'academic_year')
    list_filter = ('academic_year', 'school_class', 'subject')
    search_fields = ('school_class__name', 'subject__name', 'teacher__username')


@admin.register(StudentClassEnrollment)
class StudentClassEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'school_class', 'academic_year', 'joined_at')
    list_filter = ('academic_year', 'school_class')
    search_fields = ('student__username', 'student__profile__national_id')

# Register your models here.
