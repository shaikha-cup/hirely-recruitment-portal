from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("dashboard/", views.candidate_dashboard, name="candidate_dashboard"),

    path(
    "admin-dashboard/",
    views.admin_dashboard,
    name="admin_dashboard",
),

    path("jobs/", views.job_list, name="job_list"),

    path(
    "jobs/<int:job_id>/",
    views.job_detail,
    name="job_detail",
),

path(
    "jobs/<int:job_id>/apply/",
    views.apply_job,
    name="apply_job",

),

path(
        "admin-dashboard/",
        views.admin_dashboard,
        name="admin_dashboard",
    ),

    path(
        "admin-dashboard/application/<int:application_id>/status/",
        views.update_application_status,
        name="update_application_status",
    ),
]