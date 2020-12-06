from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from scraper.utilities.microsoft_ml_blog_scraper import MicrosoftScraper
from scraper.utilities.mlm_scraper import MLMasteryScraper

microsoft_blog = MicrosoftScraper("https://docs.microsoft.com/en-us/archive/blogs/machinelearning/")
mlm_blog = MLMasteryScraper("https://machinelearningmastery.com/blog/")

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
def get_all_blogs():
    microsoft_blog_list = microsoft_blog.get_latest_blogs()
    mlm_blog_list = mlm_blog.get_latest_blogs()
    return microsoft_blog_list, mlm_blog_list
