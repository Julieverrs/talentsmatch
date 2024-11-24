from django.contrib import admin
from django.urls import path
from jobpostings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobpostings/post-job/', views.job_posting_view, name='post-job'),
    path('jobpostings/admin/', views.admin_view, name='admin'),
    path('jobpostings/delete-job/<int:job_id>/', views.delete_job, name='delete-job'),  # Added delete URL
]
