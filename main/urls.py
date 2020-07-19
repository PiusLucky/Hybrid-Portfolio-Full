from django.urls import path, re_path, include
from main.views import (
    landing,
    backend,
    postStack,
    postPortf,
    postArch,
    post_contact
)
urlpatterns = [
        path(r'', landing, name="landing"),
        path(r'backend/', backend, name="backend"),
        path(r'post/stack/', postStack, name ='post_tech'),
        path(r'post/portf/', postPortf, name ='post_portf'),
        path(r'post/arch/', postArch, name ='post_arch'),
        path(r'post/contact/', post_contact, name="post_contact"),
       
        ]