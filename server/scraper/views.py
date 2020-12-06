from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from scraper.utilities.microsoft_ml_blog_scraper import MicrosoftScraper
from scraper.utilities.mlm_scraper import MLMasteryScraper
from scraper.utilities.spectator_scraper import SpectatorScraper

microsoft_blog = MicrosoftScraper("https://docs.microsoft.com/en-us/archive/blogs/machinelearning/")
mlm_blog = MLMasteryScraper("https://machinelearningmastery.com/blog/")
spectator_blog = SpectatorScraper("http://blog.shakirm.com/")

# Create your views here.
@csrf_exempt
def get_microsoft_blog(request, list_count=5):
    m_res = microsoft_blog.get_latest_blogs(count=int(list_count))
    return HttpResponse(m_res)

@csrf_exempt
def get_mlm_blog(request, list_count=5):
    mlm_res = mlm_blog.get_latest_blogs(count=int(list_count))
    return HttpResponse(mlm_res)

@csrf_exempt
def get_spectator_blog(request, list_count=5):
    spectator_res = spectator_blog.get_latest_blogs(count=int(list_count))
    return HttpResponse(spectator_res)

@csrf_exempt
def get_all_blogs():
    microsoft_blog_list = microsoft_blog.get_latest_blogs()
    mlm_blog_list = mlm_blog.get_latest_blogs()
    spectator_blog_list = spectator_blog.get_latest_blogs()
    return microsoft_blog_list, mlm_blog_list, spectator_blog_list
