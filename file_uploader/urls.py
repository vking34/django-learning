from django.conf.urls import url

from . import views


app_name = 'fuloader'
urlpatterns = [
    url(r'^$', views.fileUploaderView, name="fileUploader"),
]