from django.conf.urls.defaults import *
from bill.models import Category

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list',
        { 'queryset': Category.objects.all() }, 'bill_category_list'),
    (r'^(?P<slug>[-\w]+)/$', 'bill.views.category_detail'),
)
