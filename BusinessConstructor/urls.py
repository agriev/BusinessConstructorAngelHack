from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'BCApp.views.home', name='home'),
    url(r'^models$', 'BCApp.views.model_list', name='model_list'),
    url(r'^sign_in$', 'BCApp.views.sign_in', name='sign_in'),
    url(r'^recover_password$', 'BCApp.views.recover_password', name='recover_password'),
    url(r'^sign_up$', 'BCApp.views.sign_up', name='sign_up'),
    url(r'^user_profile$', 'BCApp.views.user_profile', name='user_profile'),
    #url(r'^index$', 'BCApp.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
