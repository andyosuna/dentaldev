from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ActividadesClinicas.views import Interrogatorio
from ActividadesClinicas.views import Odontograma
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'expedientedental.views.home', name='home'),
    # url(r'^expedientedental/', include('expedientedental.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^',include('altas.urls')),
    # Uncomment the next line to enable the admin:
    uurlpatterns = patterns('notasmedicas.views',
                      url(r'^admin/', include(admin.site.urls)),
                      
                      url(r'^odontograma/$', Odontograma, name='odontograma'),
                      
                      #url(r'^interrogatoriomaxilofacial/$', interrogatoriomaxilofacial, name='interrogatoriomaxilofacial'),
                      url(r'^interrogatorio/$', Interrogatorio, name='interrogatorio'),
                      )
                     # url(r'^datospaciente/$', adddatospaciente),)


    	
    
)
