from django.contrib	import admin
from altas.models import Medico
from altas.models import Paciente

#class MedicoAdmin(admin.ModelAdmin):
#	list_display = ('Nombre')
#	list_filter = ('Nombre')
#	search_fields = ['Nombre']
#	fields = ('Nombre')

#class PacienteAdmin(admin.ModelAdmin):
#	list_display = ('Nombre')
#	list_filter = ('Nombre')
#	search_fields = ['Nombre']
#	fields = ('Nombre')

admin.site.register(Medico)
admin.site.register(Paciente)