from django.conf.urls.defaults import patterns, url
from cotizacion.views import CotizacionPDF, CotizacionList

urlpatterns = patterns(
    'cotizacion.views',

    # review the items in cotizacion, select approved items
    url(r'^(?P<odontograma_id>\d+)/$', 'cotizacion_detail'),

)
urlpatterns += patterns(
    '',

    url(r'^$', CotizacionList.as_view()),


    # reporte de cotizacion
    url(r'^cotizacion/(?P<cotizacion_id>\d+)/pdf/$',
        CotizacionPDF.as_view()),
)
