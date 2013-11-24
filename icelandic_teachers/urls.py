from django.conf.urls import patterns, include, url
from teachers import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'icelandic_teachers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^genres/$', 'teachers.views.show_genres'),
)
