from django.conf.urls import url
from scraper import views

urlpatterns = [
    url(r'microsoft', views.get_microsoft_blog)
]