from django.db import models

class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    required_skills = models.TextField()
    experience_level = models.IntegerField()  # IntegerField for numeric comparison

    def __str__(self):
        return self.title

class ApplicantRecommendation(models.Model):
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='recommendations')
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    skills = models.TextField()
    experience = models.IntegerField()

    def __str__(self):
        return f"Recommendation for {self.job_posting.title}: {self.name}"
