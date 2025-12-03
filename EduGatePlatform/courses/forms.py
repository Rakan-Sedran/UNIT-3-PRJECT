from django import forms
from django.contrib.auth.models import User
from .models import SchoolClass, Subject, ClassSubject, StudentClassEnrollment
from accounts.models import Profile

class ClassSubjectForm(forms.ModelForm):
    class Meta:
        model = ClassSubject
        fields = ["school_class", "subject", "teacher", "academic_year"]
        widgets = {
            "school_class": forms.Select(attrs={"class": "form-select"}),
            "subject": forms.Select(attrs={"class": "form-select"}),
            "teacher": forms.Select(attrs={"class": "form-select"}),
            "academic_year": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        teacher_ids = Profile.objects.filter(role="teacher").values_list("user_id", flat=True)
        self.fields["teacher"].queryset = User.objects.filter(id__in=teacher_ids)


class StudentEnrollmentForm(forms.ModelForm):
    class Meta:
        model = StudentClassEnrollment
        fields = ["school_class", "student"]
        widgets = {
            "school_class": forms.Select(attrs={"class": "form-select"}),
            "student": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        student_ids = Profile.objects.filter(role="student").values_list("user_id", flat=True)
        self.fields["student"].queryset = User.objects.filter(id__in=student_ids)
