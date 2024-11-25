from django.shortcuts import render, redirect, get_object_or_404
from .models import JobPosting, ApplicantRecommendation
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

            # Save the recommendations to the database
            for applicant in recommended_applicants:
                ApplicantRecommendation.objects.create(
                    job_posting=job,
                    name=applicant.get('Name'),
                    job_title=applicant.get('Job_Title'),
                    skills=applicant.get('Skills'),
                    experience=applicant.get('Experience'),
                )

            # Render the job_posted.html template with the job details and recommended applicants
            return render(request, 'jobpostings/job_posted.html', {
                'job': job,  # Pass the job object
                'recommended_applicants': recommended_applicants
            })
    else:
        form = JobPostingForm()

    return render(request, 'jobpostings/job_posting_form.html', {'form': form})

def admin_view(request):
    # Fetch all job postings with related recommendations
    job_postings = JobPosting.objects.prefetch_related('recommendations')

    # Pass the job postings and their recommendations to the template
    return render(request, 'jobpostings/admin.html', {'job_postings': job_postings})


def delete_job(request, job_id):
    # Get the job posting by its ID
    job = get_object_or_404(JobPosting, id=job_id)

    # Delete the job posting
    job.delete()

    # Redirect back to the admin page
    return redirect('admin')
