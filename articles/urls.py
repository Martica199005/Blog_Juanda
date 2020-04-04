from django.conf.urls import url
from . import views

app_name='articles'

urlpatterns = [
  url(r'^$', views.articles_list,name="list"),
  url(r'^article_subject/$',views.article_subject,name="article_subject"),
  url(r'^articles_nutrition/$',views.articles_nutrition,name="articles_nutrition"),
  url(r'^articles_massages/$', views.articles_massages,name="articles_massages"),
  url(r'^create/$',views.article_create,name="create"),
  url(r'^(?P<slug>[\w-]+)/$', views.articles_details,name="detail"),
  url(r'^delete_article/(?P<slug>[\w-]+)/$', views.delete_article,name="delete_article"),
]