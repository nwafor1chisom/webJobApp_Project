from django.urls import path
from . import views

urlpatterns = [
    # Job Seeker Views
    path('', views.job_list_view, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail_view, name='job_detail'),

    # Employer Views
    path('employer/jobs/', views.employer_jobs_view, name='employer_jobs'),
    path('employer/jobs/create/', views.create_job_view, name='create_job'),
    path('employer/jobs/<int:pk>/edit/', views.edit_job_view, name='edit_job'),
    path('employer/jobs/<int:pk>/delete/', views.delete_job_view, name='delete_job'),
]
