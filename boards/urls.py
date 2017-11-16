from django.conf.urls import url

from . import views

app_name = 'boards'
urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^(?P<board_id>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
]