from django.conf.urls import url
from stu.views import *

urlpatterns = [
    url(r'^$', login),
    url(r'^index/', index),
    url(r'^n1/', n1),
    url(r'^z1/', z1),
    url(r'^plat/', plat),
    url(r'^game1/', game1),
    url(r'^game2/', game2),
    url(r'^art/', art),
]
