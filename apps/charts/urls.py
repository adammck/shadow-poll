from django.conf.urls.defaults import *
import charts.views as views

urlpatterns = patterns('charts',
                       (r'^charts/$', 'views.current_status'),
                       (r'^map/$', 'views.show_stats_on_map'),
                       (r'^data/(?P<path>.*)$','views.data'),
                       (r'^get_stat/$', 'views.get_stats')
                       )

handler404 = 'charts.views.view_404'
handler500 = 'charts.views.view_500'
