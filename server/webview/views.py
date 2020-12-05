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
    blog_list = get_all_blogs()
    context["blog_list"] = blog_list
    return render(request, "index.html", context)
