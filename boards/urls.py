from django.conf.urls import url

from . import views

app_name = 'boards'
urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^(?P<board_id>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^(?P<board_id>\d+)/topic(?P<topic_id>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    url(r'^(?P<board_id>\d+)/topic(?P<topic_id>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    url(r'^(?P<board_id>\d+)/topic(?P<topic_id>\d+)/post(?P<post_pk>\d+)/edit/', views.PostUpdateView.as_view(), name='edit_post'),
]