from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import JobPost
from .forms import JobPostForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone


# For Job Seekers
def job_list_view(request):
    query = request.GET.get('q')
    jobs = JobPost.objects.filter(deadline__gte=timezone.now()).order_by('-created_at')

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(location__icontains=query) |
            Q(category__icontains=query)
        )

    paginator = Paginator(jobs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'jobs/job_list.html', {'page_obj': page_obj})

def job_detail_view(request, pk):
    job = get_object_or_404(JobPost, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

# For Employers
@login_required
def create_job_view(request):
    if not request.user.is_employer():
        return redirect('dashboard')

    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            return redirect('employer_jobs')
    else:
        form = JobPostForm()

    return render(request, 'jobs/job_form.html', {'form': form})

@login_required
def employer_jobs_view(request):
    if not request.user.is_employer():
        return redirect('dashboard')

    jobs = JobPost.objects.filter(employer=request.user).order_by('-created_at')
    return render(request, 'jobs/employer_jobs.html', {'jobs': jobs})

@login_required
def edit_job_view(request, pk):
    job = get_object_or_404(JobPost, pk=pk, employer=request.user)

    if request.method == 'POST':
        form = JobPostForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('employer_jobs')
    else:
        form = JobPostForm(instance=job)

    return render(request, 'jobs/job_form.html', {'form': form})

@login_required
def delete_job_view(request, pk):
    job = get_object_or_404(JobPost, pk=pk, employer=request.user)
    job.delete()
    return redirect('employer_jobs')
