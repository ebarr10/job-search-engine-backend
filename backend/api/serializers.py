from rest_framework import serializers
from jobspy.scrapers import Site


class JobSerializer(serializers.Serializer):
  site = serializers.ChoiceField(choices=[(site.value, site.name) for site in Site])

  # Job Posting
  title = serializers.CharField(max_length=255)
  company = serializers.CharField(max_length=255)
  company_url = serializers.URLField(allow_blank=True)
  job_url = serializers.URLField(max_length=500)
  location = serializers.CharField(max_length=255)
  description = serializers.CharField(max_length=1000, allow_blank=True)
  job_type = serializers.CharField(max_length=12, allow_blank=True)
  interval = serializers.CharField(max_length=255)
  min_amount = serializers.CharField(max_length=255, allow_blank=True)
  max_amount = serializers.CharField(max_length=255, allow_blank=True)
  currency = serializers.CharField(max_length=255, allow_blank=True)
  salary_source = serializers.CharField(max_length=255, allow_blank=True)
  date_posted = serializers.DateField()
  is_remote = serializers.BooleanField(default=False)
  emails = serializers.CharField(max_length=255, allow_blank=True)

  # LinkedIn Specific
  job_level = serializers.CharField(max_length=12, allow_blank=True)

  # LinkedIn & Indeed Specific
  company_industry = serializers.CharField(max_length=255, allow_blank=True)

  # Indeed Specific
  company_logo = serializers.URLField(allow_blank=True)
  company_description = serializers.CharField(max_length=500, allow_blank=True)