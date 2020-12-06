from django.conf.urls import url
from scraper import views

urlpatterns = [
    url(r'microsoft/(\d+)', views.get_microsoft_blog),
    url(r'microsoft', views.get_microsoft_blog),
    url(r'mlm/(\d+)', views.get_mlm_blog),
    url(r'mlm', views.get_mlm_blog),
]