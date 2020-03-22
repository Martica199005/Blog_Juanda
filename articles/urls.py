from django.conf.urls import url
from . import views

app_name='articles'

urlpatterns = [
    url(r'^$', views.articles_list,name="list"), 
    url(r'^(?P<slug>[\w-]+)/$', views.articles_details,name="detail"),  

]