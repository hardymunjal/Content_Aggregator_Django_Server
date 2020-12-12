from django.conf.urls import url
from scraper import views

urlpatterns = [
    url(r'microsoft/(\d+)', views.get_microsoft_blog),
    url(r'microsoft', views.get_microsoft_blog),
    url(r'mlm/(\d+)', views.get_mlm_blog),
    url(r'mlm', views.get_mlm_blog),
    url(r'spectator/(\d+)', views.get_spectator_blog),
    url(r'spectator', views.get_spectator_blog),
    url(r'fastml/(\d+)', views.get_fastml_blog),
    url(r'fastml', views.get_fastml_blog),
]