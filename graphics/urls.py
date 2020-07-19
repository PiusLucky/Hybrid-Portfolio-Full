from django.urls import path, re_path, include
from graphics.views import graphics, archive_detail


urlpatterns = [

 path(r'', graphics, name="graphics"),
 re_path(r'^(?P<slug>[-\w]+)/$', archive_detail, name='detail'),

]