"""djangoLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import signup
from . import views

from django.contrib.auth import views as auth_views

# app_name = "home", for urls of the main,
# the app_name dont need to created
# cause Django engine consider from here to sub-urls.

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', signup, name='signup'),
    url(r'^', include('accounts.urls'), name='accounts'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^password-reset/', include('password-reset.urls'), name='password-reset'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
    url(r'^register/', include('user_auth.urls'), name='register'),
    url(r'^polls/', include('polls.urls'), name='polls'),
    url(r'^file-uploader/', include('file_uploader.urls'), name='file-uploader'),
    url(r'^pagination/', include('pagination.urls'), name='pagination'),
    url(r'^login/', include('login.urls'), name='login'),
    url(r'^boards/', include('boards.urls'), name='boards'),
    url(r'^admin/', admin.site.urls, name='admin'),
]
