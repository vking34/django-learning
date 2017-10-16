from django.conf.urls import url

from . import views

urlpatterns = [
    # ./register/
    url(r'^$', views.register),
]