from django.db import models

class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    required_skills = models.TextField()
    experience_level = models.IntegerField()  # Change to IntegerField for numeric comparison

    def __str__(self):
        return self.title
