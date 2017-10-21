from django.conf.urls import url, include, patterns

urlpatterns = patterns('login.views',
                       url(r'^login/', 'loginView'),
                       url(r'^greeting/', 'formView'),
                       url(r'^logout/', 'logoutView')
                       )