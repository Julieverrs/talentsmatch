from django.contrib import admin
from django.urls import path
from jobpostings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobpostings/post-job/', views.job_posting_view, name='post-job'),
]
