from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json

from scraper.utilities.microsoft_ml_blog_scraper import MicrosoftScraper
from scraper.utilities.mlm_scraper import MLMasteryScraper
from scraper.utilities.spectator_scraper import SpectatorScraper
from scraper.utilities.fastml_scraper import FastMLScraper

microsoft_blog = MicrosoftScraper("https://docs.microsoft.com/en-us/archive/blogs/machinelearning/")
mlm_blog = MLMasteryScraper("https://machinelearningmastery.com/blog/")
spectator_blog = SpectatorScraper("http://blog.shakirm.com/")
fastml_blog = FastMLScraper("http://fastml.com/")

# Create your views here.
@csrf_exempt
def get_microsoft_blog(request, list_count=5):
    m_res = microsoft_blog.get_latest_blogs(count=int(list_count))
    return JsonResponse(m_res, safe=False)

@csrf_exempt
def get_mlm_blog(request, list_count=5):
    mlm_res = mlm_blog.get_latest_blogs(count=int(list_count))
    return JsonResponse(mlm_res, safe=False)

@csrf_exempt
def get_spectator_blog(request, list_count=5):
    spectator_res = spectator_blog.get_latest_blogs(count=int(list_count))
    return JsonResponse(spectator_res, safe=False)

@csrf_exempt
def get_fastml_blog(request, list_count=5):
    fastml_res = fastml_blog.get_latest_blogs(count=int(list_count))
    return JsonResponse(fastml_res, safe=False)

@csrf_exempt
def get_all_blogs():
    microsoft_blog_list = microsoft_blog.get_latest_blogs()
    mlm_blog_list = mlm_blog.get_latest_blogs()
    spectator_blog_list = spectator_blog.get_latest_blogs()
    fastml_blog_list = fastml_blog.get_latest_blogs()
    return microsoft_blog_list, mlm_blog_list, spectator_blog_list, fastml_blog_list
