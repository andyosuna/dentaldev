from django.db import models

from core.models import Grupo
from ActividadesClinicas.models import Tratamiento


class PrecioTratamiento(models.Model):
	tratamiento = models.ForeignKey(Tratamiento)
	grupo = models.ForeignKey(Grupo)
	precio = models.DecimalField(max_digits=19, decimal_places=3)

	def __unicode__(self):
		return "%s (%s)"%(self.tratamiento, self.precio)
