from django.conf.urls import url
from stu.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^index/', index),
    url(r'^stuffinfo/', stuffinfo),
    url(r'^deptsetting/', dept_setting),
    url(r'^projsetting/', proj_setting),
    url(r'^stuffsearch/', stuff_search),
]
