from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render

from scraper.views import get_all_blogs
# Create your views here.

@csrf_exempt
def test(request):
    return HttpResponse("Server Runnning...")

@csrf_exempt
def index(request):
    context={}
    microsoft_blog_list, mlm_blog_list = get_all_blogs()
    context["microsoft"] = microsoft_blog_list
    context["mlm"] = mlm_blog_list
    return render(request, "index.html", context)
