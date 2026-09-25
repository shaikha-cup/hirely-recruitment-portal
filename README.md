# Hirely — Recruitment & Job Application Portal

Hirely is a modern recruitment and job application portal built with Python and Django.

The platform provides separate experiences for candidates and recruiters, allowing candidates to discover jobs and track applications while recruiters manage job openings and candidate applications.

---

## ✨ Features

### Candidate Features

- Candidate registration
- Secure login and logout
- Browse available jobs
- Search jobs by title, company, or location
- View detailed job information
- Apply for jobs
- Upload CV / Resume
- Optional cover letter
- CV file type validation
- CV file size validation
- Duplicate application protection
- View application history
- Track application status

### Recruiter Features

- Secure recruiter authentication
- Recruiter dashboard
- Job statistics
- Application statistics
- Add job openings
- Edit job openings
- Delete job openings
- Activate / deactivate job openings
- View all candidate applications
- View candidate information
- View uploaded CVs
- Update application status

### Application Statuses

- Applied
- Shortlisted
- Interview
- Rejected

---

## 🎨 UI / UX

Hirely uses a modern recruitment SaaS-inspired interface featuring:

- Premium dark visual design
- Glassmorphism
- Gradient accents
- Modern typography
- Responsive layouts
- Mobile navigation
- Hover interactions
- Scroll reveal animations
- Micro-interactions
- Responsive application forms
- Candidate dashboard
- Recruiter dashboard
- Toast notification system

---

## 🛠️ Technology Stack

### Backend

- Python
- Django

### Database

- SQLite

### Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap Icons

### File Handling

- Pillow
- Django Media Files

---

## 📁 Project Structure

```text
recruitment-portal/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── portal/
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── auth/
│   ├── candidate/
│   ├── jobs/
│   ├── admin_dashboard/
│   ├── home.html
│   └── base.html
│
├── static/
│   ├── css/
│   └── js/
│
├── media/
│   └── cvs/
│
├── manage.py
├── requirements.txt
└── README.md