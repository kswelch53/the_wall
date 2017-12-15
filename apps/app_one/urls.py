from django.conf.urls import url
from . import views

urlpatterns = [
# from root route to index method
    url(r'^$', views.index),
    url(r'index^$', views.index, name="index"),
    url(r'^post_message$', views.post_message, name="post_message"),
    # url(r'^post_comment$', views.post_comment, name="post_comment"),
    url(r'^post_comment/(?P<ms_id>\d+)$', views.post_comment, name="post_comment"),
    url(r'^logoff$', views.logoff, name="logoff"),
]
