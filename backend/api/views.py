import pandas as pd 
from jobspy import scrape_jobs
from requests import Response
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView


class ScrapeJobsView(APIView):

  def gather_site_name(self, filtered_sites):
    if filtered_sites == "":
      return ["indeed", "linkedin", "zip_recruiter", "glassdoor", "google"]
    else:
      return [filtered_sites]
    
  def get_is_remote(self, is_remote):
    return True if is_remote == 'true' else False

  def get(self, request, *args, **kwargs):
    search_field = request.GET.get("searchTerm", "")
    location = request.GET.get("location", "")
    site = request.GET.get("siteName", "")
    is_remote = request.GET.get("isRemote", "")
    job_type = request.GET.get("jobType", "")

    jobs_dataframe = scrape_jobs(
      site_name=self.gather_site_name(site),
      search_term=search_field,
      google_search_term=search_field,
      location=location,
      job_type=job_type,
      is_remote=self.get_is_remote(is_remote),
      results_wanted=20,
      country_indeed='USA',
    )
    
    # remove any NaN
    jobs_dataframe = jobs_dataframe.where(pd.notnull(jobs_dataframe), None)

    jobs = jobs_dataframe.to_dict(orient='records')    

    jobs_serializer = JobSerializer(data=jobs, many=True)
    jobs_serializer.is_valid(raise_exception=False)

    response = Response(jobs_serializer.data)
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = 'application/json'
    return response