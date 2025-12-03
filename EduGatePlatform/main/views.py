from django.shortcuts import render, redirect
from .models import Announcement
from django.utils import timezone
from django.db import models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from accounts.models import Profile
from .forms import SchoolClassForm, AnnouncementForm

# Create your views here.

def home(request):
    today = timezone.now().date()
    announcements = Announcement.objects.filter(
        models.Q(start_date__isnull=True) | (models.Q(start_date__lte=today)),
        models.Q(end_date__isnull=True) | (models.Q(end_date__gte=today))
    ).order_by('-is_important', '-created_at')[:6]

    context = {
        'announcements': announcements,
    }
    return render(request, 'main/home.html', context)

@login_required
def create_class(request):
    profile = getattr(request.user, "profile", None)

    if not (request.user.is_superuser or (profile and profile.role == "admin")):
        return HttpResponseForbidden("Only administrators can create classes.")

    if request.method == "POST":
        form = SchoolClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:dashboard")
    else:
        form = SchoolClassForm()

    return render(request, "main/create_class.html", {"form": form})

@login_required
def add_announcement(request):
    profile = getattr(request.user, "profile", None)

    if not (request.user.is_superuser or (profile and profile.role == "admin")):
        return HttpResponseForbidden("Only administrators can add announcements.")

    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:dashboard")
    else:
        form = AnnouncementForm()

    return render(request, "main/add_announcement.html", {"form": form})
