from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from wkhtmltopdf.views import PDFTemplateView

from cotizacion.models import Cotizacion, CotizacionItem
from cotizacion.forms import ItemFormSet
from clinica.models import Odontograma


class CotizacionList(ListView):
    model = Odontograma
    context_object_name = 'orders'
    template_name = 'cotizaciones.html'


def cotizacion_detail(request, odontograma_id):
    odontograma = get_object_or_404(Odontograma, pk=odontograma_id)
    try:
        cotizacion = odontograma.cotizacion_set.get()
        items = cotizacion.cotizacionitem_set.all()

    except Cotizacion.DoesNotExist:
        cotizacion = Cotizacion.objects.create(odontograma=odontograma)
        CotizacionItem.objects.create_items(cotizacion)
        items = cotizacion.cotizacionitem_set.all()

    if request.method == 'POST':
        formset = ItemFormSet(request.POST)

        if formset.is_valid():
            formset.save()

    else:
        formset = ItemFormSet(queryset=items)

    total = cotizacion.total_aceptado()

    return render(request, 'cotizacion.html', {
                  'cotizacion': cotizacion,
                  'items': items,
                  'formset': formset,
                  'total': total
                  })



class CotizacionPDF(PDFTemplateView):
    filename = 'cotizacion.pdf'
    template_name = 'printit.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kwargs):
        context = super(CotizacionPDF, self).get_context_data(**kwargs)
        self.cotizacion_id = int(kwargs.get('cotizacion_id'))
        cotizacion = get_object_or_404(Cotizacion, pk=self.cotizacion_id)
        context['cotizacion'] = cotizacion
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context
