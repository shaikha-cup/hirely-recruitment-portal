# Hirely — Recruitment & Job Application Portal

Hirely is a modern recruitment and job application portal built with Python and Django.

The platform provides separate experiences for candidates and recruiters. Candidates can discover available jobs, apply for positions, upload their CVs, and track application statuses. Recruiters can manage job openings and candidate applications through a dedicated dashboard.

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

## 📌 Application Statuses

- Applied
- Shortlisted
- Interview
- Rejected

## 🎨 UI / UX

Hirely uses a modern recruitment SaaS-inspired interface featuring:

- Premium dark visual design
- Glassmorphism-inspired components
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
- Smooth user interactions

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
│   ├── fixtures/
│   │   └── sample_data.json
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
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/shaikha-cup/hirely-recruitment-portal.git
cd hirely-recruitment-portal
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Load sample job data

```bash
python manage.py loaddata sample_data
```

### 7. Create an admin / recruiter account

```bash
python manage.py createsuperuser
```

Follow the prompts to create the administrator account.

### 8. Start the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## 🔐 Authentication & Permissions

Hirely uses Django's built-in authentication system.

### Candidates

Candidates can:

- Register an account
- Log in and log out
- Browse active jobs
- Submit applications
- Upload CVs
- View their own application history
- Track application status

### Recruiters / Administrators

Authorized staff users can:

- Access the recruiter dashboard
- Create, edit and delete jobs
- Activate or deactivate job openings
- View candidate applications
- View uploaded CVs
- Update application statuses

Unauthorized users cannot access recruiter-only dashboard functionality.

## 📄 CV Validation

Uploaded CVs are validated before being saved.

Supported formats:

- PDF
- DOC
- DOCX

Maximum allowed file size:

**5 MB**

Duplicate applications for the same candidate and job are prevented.

## 🗃️ Sample Data

Sample job data is included in:

```text
portal/fixtures/sample_data.json
```

Load the sample data using:

```bash
python manage.py loaddata sample_data
```

The local SQLite database is not included in the repository.

## 🔑 Demo Access

### Recruiter / Admin

Create a recruiter/admin account locally using:

```bash
python manage.py createsuperuser
```

### Candidate

Candidate accounts can be created from the registration page:

```text
http://127.0.0.1:8000/register/
```

For security reasons, passwords and GitHub access tokens are not stored in this repository.

## 🌐 Main Application Routes

| Route | Purpose |
|---|---|
| `/` | Home page |
| `/register/` | Candidate registration |
| `/login/` | Login |
| `/logout/` | Logout |
| `/jobs/` | Browse and search jobs |
| `/jobs/<id>/` | Job details |
| `/jobs/<id>/apply/` | Apply for a job |
| `/dashboard/` | Candidate dashboard |
| `/admin-dashboard/` | Recruiter dashboard |
| `/admin/` | Django administration |

## 🔒 Security & Validation

The project uses Django's built-in security features, including:

- CSRF protection
- Authentication
- Login-required views
- Staff permission checks
- Form validation
- File extension validation
- File size validation
- Duplicate application protection
- Django ORM for database operations

Sensitive files such as the local database, virtual environment, uploaded media, and environment files are excluded using `.gitignore`.

## 📊 Database Relationships

The project contains two main application models:

### Job

Stores information about job openings, including:

- Job title
- Company
- Location
- Description
- Requirements
- Salary
- Job type
- Active status
- Creation date

### Application

Connects a candidate with a job through relationships with Django's `User` model and the `Job` model.

Each application stores:

- Candidate
- Job
- CV
- Cover letter
- Application status
- Application date

A unique constraint prevents the same candidate from applying to the same job more than once.

## 🎯 Project Objective

The objective of Hirely is to provide a complete recruitment workflow where candidates can discover and apply for jobs while recruiters can efficiently manage job openings and candidate applications through a centralized system.

## 📸 Project Demonstration

Screenshots included with the project submission can demonstrate:

- Home page
- Job listing
- Job details
- Candidate registration
- Application form
- Candidate dashboard
- Recruiter dashboard
- Job management
- Application status management
- GitHub repository

## 👩‍💻 Project

**Hirely — Recruitment & Job Application Portal**

Built using:

**Python + Django + SQLite + HTML + CSS + JavaScript**
