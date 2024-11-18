# jobpostings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('post-job/', views.job_posting_view, name='job_posting'),
]
