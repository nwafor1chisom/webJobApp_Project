🧑‍💼 Job Board Web Application

A full-featured Job Board platform built with Django, allowing employers to post job listings and job seekers to find and apply for them.
This project demonstrates a scalable, production-ready architecture with authentication, role-based access control, file uploads, email notifications, and admin management.

🚀 Project Overview

The Job Board Web Application connects employers and job seekers in a seamless workflow:

Employers can create and manage job postings, review applicants, and receive email notifications.

Job seekers can browse, filter, and apply for jobs by uploading their resumes and cover letters.

Admins have full control over users, jobs, and applications from a centralized dashboard.

🧩 Core Features
👥 1. User Authentication & Roles

User registration and login system.

Separate dashboards for employers and job seekers.

Role-based access using Django groups or a custom user model.

💼 2. Job Posting & Management

Employers can create, edit, and delete job posts.

Job listings include: title, description, company, location, salary range, deadline, and category.

Employers can view a list of applicants per job.

🔍 3. Job Listings for Job Seekers

Paginated and filterable job listings (location, category, salary, date).

Dedicated job detail pages with an “Apply Now” option.

📄 4. Application System

Job seekers can apply with a cover letter and resume (PDF/DOC).

Applications are linked to both the user and the job post.

Employers can view and download resumes directly.

🛠️ 5. Admin Panel

Superadmin manages all users, jobs, and applications.

Centralized control for site administration and data management.

📧 6. Email Notifications

Sends confirmation email when a user applies for a job.

Sends notification to the employer about new applications.

🧱 Tech Stack
Layer	Technology
Frontend	Django Templates, Bootstrap
Backend	Django (Python)
Database	PostgreSQL / SQLite
File Handling	Django FileField, MEDIA_ROOT, MEDIA_URL
Authentication	Django’s built-in Auth system
Email System	Django Email Backend (Console for Dev)


⚙️ Installation & Setup
Prerequisites
  Python 3.10+
  Git
  Virtual Environment (recommended)

⚙️ How to Deploy
1️⃣ Clone the repository
  git clone https://github.com/nwafor1chisom/webJobApp_Project.git
  cd webJobApp_Project

