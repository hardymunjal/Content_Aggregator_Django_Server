from django.conf.urls import url
from webview import views

urlpatterns = [
    url(r'testserver', views.test),
    url(r'webpage', views.index)
]