from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm
from .models import Application
from jobs.models import JobPost
from django.core.mail import send_mail
from django.conf import settings

@login_required
def apply_job_view(request, pk):
    job = get_object_or_404(JobPost, pk=pk)

    if not request.user.is_job_seeker():
        return redirect('dashboard')

    if Application.objects.filter(user=request.user, job=job).exists():
        return render(request, 'applications/already_applied.html', {'job': job})

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()

            # Email notifications
            send_mail(
                subject='Application Submitted Successfully',
                message=f'You have successfully applied for {job.title} at {job.company_name}.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.user.email],
            )

            send_mail(
                subject='New Job Application Received',
                message=f'{request.user.username} has applied for your job post: {job.title}.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[job.employer.email],
            )

            return render(request, 'applications/application_success.html', {'job': job})
    else:
        form = ApplicationForm()

    return render(request, 'applications/apply.html', {'form': form, 'job': job})

@login_required
def view_applications_view(request, pk):
    job = get_object_or_404(JobPost, pk=pk, employer=request.user)
    applications = job.applications.select_related('user').all()
    return render(request, 'applications/application_list.html', {'job': job, 'applications': applications})

