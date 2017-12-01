from django.conf.urls import url

from . import views

app_name='accounts'

urlpatterns = [
    url(r'^settings/account/', views.UserUpdateView.as_view(), name='my_account'),
]