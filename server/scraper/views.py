from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from scraper.utilities.microsoft_ml_blog_scraper import MicrosoftScraper


microsoft_blog = MicrosoftScraper("https://docs.microsoft.com/en-us/archive/blogs/machinelearning/")

# Create your views here.
@csrf_exempt
def get_microsoft_blog(request):
    m_res = microsoft_blog.get_latest_blogs()
    return HttpResponse(m_res)

def get_all_blogs():
    microsoft_blog_list = microsoft_blog.get_latest_blogs()
    return microsoft_blog_list
