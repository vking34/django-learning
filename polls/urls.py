from django.conf.urls import url

from . import views

app_name = "polls"
urlpatterns = [
    # /polls/
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.indexView.as_view(), name='index'),
    # /polls/details/<question_id>/
    # url(r'^details/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.detailView.as_view(), name='detail'),
    # /polls/<question_id>/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.resultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]