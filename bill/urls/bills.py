from django.conf.urls.defaults import *
from bill.models import Bill

entry_info_dict = {
   'queryset': Bill.objects.all(),
   'date_field': 'due_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    (r'^$', 'archive_index', entry_info_dict, 'bill_archive_index'),
    (r'^(?P<year>\d{4})/$', 'archive_year', entry_info_dict, 'bill_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month', entry_info_dict, 'bill_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', entry_info_dict, 'bill_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', entry_info_dict, 'bill_detail'),
)
