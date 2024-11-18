from django.shortcuts import render
from .forms import JobPostingForm
from .ml_model import recommend_applicants

def job_posting_view(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            # Save the job posting (this part is handled by your form)
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


def home(request):
    return render(request, 'home.html')

