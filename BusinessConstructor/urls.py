from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'BCApp.views.home', name='home'),
    url(r'^models$', 'BCApp.views.model_list', name='model_list'),
    url(r'^signin$', 'BCApp.views.sign_in', name='sign_in'),
    #url(r'^index$', 'BCApp.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
