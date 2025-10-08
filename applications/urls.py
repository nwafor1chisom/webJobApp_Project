from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:pk>/', views.apply_job_view, name='apply_job'),
    path('employer/applications/<int:pk>/', views.view_applications_view, name='view_applications'),
]
