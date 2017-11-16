from django.conf.urls import url

from . import views

app_name = 'register'
urlpatterns = [
    # ./register/
    url(r'^$', views.register, name='signup'),
]