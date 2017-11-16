from django.conf.urls import url
from . import views

app_name = 'pagination'
urlpatterns = [
    url(r'$', views.listing, name='list'),
]