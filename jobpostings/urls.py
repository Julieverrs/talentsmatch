from django.urls import path
from . import views

urlpatterns = [
    path('post-job/', views.job_posting_view, name='job_posting'),
    path('admin/', views.admin_view, name='admin'),  # Add this line for the admin page
]
