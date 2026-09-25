from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import models
from django.shortcuts import redirect, render, get_object_or_404

from .forms import RegistrationForm, ApplicationForm
from .models import Job, Application


def home(request):
    return render(request, "home.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Welcome to Hirely! Your account has been created."
            )

            return redirect("home")

    else:
        form = RegistrationForm()

    return render(
        request,
        "auth/register.html",
        {"form": form},
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)

            messages.success(
                request,
                f"Welcome back, {user.first_name or user.username}!"
            )

            return redirect("home")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(request, "auth/login.html")


def logout_view(request):
    logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("home")
@login_required
def candidate_dashboard(request):
    applications = request.user.applications.select_related("job")

    context = {
        "applications": applications,
        "application_count": applications.count(),
        "applied_count": applications.filter(status="Applied").count(),
        "shortlisted_count": applications.filter(status="Shortlisted").count(),
        "interview_count": applications.filter(status="Interview").count(),
        "rejected_count": applications.filter(status="Rejected").count(),
    }

    return render(
        request,
        "candidate/dashboard.html",
        context,
    )

    

    return render(
        request,
        "candidate/dashboard.html",
        context,
    )
def job_list(request):
    jobs = Job.objects.filter(is_active=True)

    query = request.GET.get("q", "").strip()

    if query:
        jobs = jobs.filter(
            models.Q(title__icontains=query)
            | models.Q(company__icontains=query)
            | models.Q(location__icontains=query)
        )

    return render(
        request,
        "jobs/job_list.html",
        {
            "jobs": jobs,
            "query": query,
        },
    )
def job_detail(request, job_id):
    job = get_object_or_404(
        Job,
        id=job_id,
        is_active=True,
    )

    already_applied = False

    if request.user.is_authenticated:
        already_applied = Application.objects.filter(
            candidate=request.user,
            job=job,
        ).exists()

    return render(
        request,
        "jobs/job_detail.html",
        {
            "job": job,
            "already_applied": already_applied,
        },
    )
@login_required
def apply_job(request, job_id):
    job = get_object_or_404(
        Job,
        id=job_id,
        is_active=True,
    )

    existing_application = Application.objects.filter(
        candidate=request.user,
        job=job,
    ).first()

    if existing_application:
        return redirect("candidate_dashboard")

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.candidate = request.user
            application.job = job
            application.status = "Applied"
            application.save()

            return redirect("candidate_dashboard")

    else:
        form = ApplicationForm()

    return render(
        request,
        "jobs/apply.html",
        {
            "job": job,
            "form": form,
        },
    )
@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect("candidate_dashboard")

    jobs = Job.objects.all()
    applications = Application.objects.select_related(
        "candidate",
        "job",
    )

    context = {
        "jobs": jobs,
        "applications": applications,
        "job_count": jobs.count(),
        "active_job_count": jobs.filter(is_active=True).count(),
        "application_count": applications.count(),
        "shortlisted_count": applications.filter(
            status="Shortlisted"
        ).count(),
        "interview_count": applications.filter(
            status="Interview"
        ).count(),
        "rejected_count": applications.filter(
            status="Rejected"
        ).count(),
    }

    return render(
        request,
        "admin_dashboard/dashboard.html",
        context,
    )
@login_required
def update_application_status(request, application_id):
    if not request.user.is_staff:
        return redirect("candidate_dashboard")

    application = get_object_or_404(
        Application,
        id=application_id,
    )

    if request.method == "POST":
        new_status = request.POST.get("status")

        valid_statuses = {
            choice[0]
            for choice in Application.STATUS_CHOICES
        }

        if new_status in valid_statuses:
            application.status = new_status
            application.save(update_fields=["status"])

    return redirect("admin_dashboard")