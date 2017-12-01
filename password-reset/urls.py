from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import templates
from . import views

app_name='password-reset'

urlpatterns = [
    url(r'^$', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ), name='reset'),
    url(r'^done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='done'),
    url(r'^(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/$)',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='confirm'),
    url(r'^complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='complete'),

]
