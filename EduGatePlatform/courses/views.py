from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from accounts.models import Profile
from .forms import ClassSubjectForm, StudentEnrollmentForm

# Create your views here.


@login_required
def assign_subject_to_class(request):
    profile = getattr(request.user, "profile", None)
    is_admin = request.user.is_superuser or (profile and profile.role == "admin")
    if not is_admin:
        return HttpResponseForbidden("Only administrators can assign subjects.")

    if request.method == "POST":
        form = ClassSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:dashboard")
    else:
        form = ClassSubjectForm()

    return render(request, "courses/assign_subject.html", {"form": form})


@login_required
def enroll_student_in_class(request):
    profile = getattr(request.user, "profile", None)
    is_admin = request.user.is_superuser or (profile and profile.role == "admin")
    if not is_admin:
        return HttpResponseForbidden("Only administrators can enroll students.")

    if request.method == "POST":
        form = StudentEnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:dashboard")
    else:
        form = StudentEnrollmentForm()

    return render(request, "courses/enroll_student.html", {"form": form})

