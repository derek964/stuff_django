from django.conf.urls import url
from stu.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^index',index),
]
