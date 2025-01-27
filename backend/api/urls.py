from django.urls import path
from .views import ScrapeJobsView

urlpatterns = [
  path('jobs/', ScrapeJobsView.as_view(), name="jobs-view"),
]