from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^signup/', "webreminder.registration.views.signup"),
    (r'^login/', 'django.contrib.auth.views.login'),
    (r'^logout/', 'django.contrib.auth.views.logout', {"next_page": "/"}),
    
    (r'^admin/(.*)', admin.site.root),
    (r'^bills/', include('bill.urls.bills')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        ),
    )
