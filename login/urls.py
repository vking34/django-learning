from django.conf.urls import url

from . import views

app_name = "login"
urlpatterns = [
    url(r'^$', views.loginView, name='login'),
    url(r'^greeting/', views.formView, name='greeting'),
    url(r'^logout/', views.logoutView, name='logout'),
]