from django.shortcuts import render, redirect, get_object_or_404
from .models import JobPosting
from .forms import JobPostingForm
from .ml_model import recommend_applicants

def job_posting_view(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            # Save the job posting
            job = form.save()

            # Get the job data from the form
            job_data = form.cleaned_data

            # Get the recommended applicants
            recommended_applicants = recommend_applicants(job_data)

            # Render the job_posted.html template with the recommended applicants
            return render(request, 'jobpostings/job_posted.html', {
                'recommended_applicants': recommended_applicants
            })
    else:
        form = JobPostingForm()

    return render(request, 'jobpostings/job_posting_form.html', {'form': form})

def admin_view(request):
    # Fetch all job postings from the database
    job_postings = JobPosting.objects.all()

    # Pass the job postings to the template
    return render(request, 'jobpostings/admin.html', {'job_postings': job_postings})

def delete_job(request, job_id):
    # Get the job posting by its ID
    job = get_object_or_404(JobPosting, id=job_id)

    # Delete the job posting
    job.delete()

    # Redirect back to the admin page
    return redirect('admin')
