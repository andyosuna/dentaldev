# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Procedimiento.odontograma'
        db.add_column('ActividadesClinicas_procedimiento', 'odontograma',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ActividadesClinicas.Odontograma'], null=True),
                      keep_default=False)

        # Removing M2M table for field odontograma on 'Procedimiento'
        db.delete_table(db.shorten_name('ActividadesClinicas_procedimiento_odontograma'))


    def backwards(self, orm):
        # Deleting field 'Procedimiento.odontograma'
        db.delete_column('ActividadesClinicas_procedimiento', 'odontograma_id')

        # Adding M2M table for field odontograma on 'Procedimiento'
        m2m_table_name = db.shorten_name('ActividadesClinicas_procedimiento_odontograma')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('procedimiento', models.ForeignKey(orm['ActividadesClinicas.procedimiento'], null=False)),
            ('odontograma', models.ForeignKey(orm['ActividadesClinicas.odontograma'], null=False))
        ))
        db.create_unique(m2m_table_name, ['procedimiento_id', 'odontograma_id'])


    models = {
        'ActividadesClinicas.historiaclinica': {
            'Comisuras': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'HistoriaClinica'},
            'adicciones': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'alergias': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'apararoGenitourinario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aparatoCardioBascular': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aparatoDigestivo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aparatoRespiratorio': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aparatoTegumentario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bolsasperiodontales': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'bordebermellon': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cabeza': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'caraAsimetria': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'carrillos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cartilladeVacunacion': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'chasquidos': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'complexion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'consumodeGolosinas': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'craneo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'credencialPaciente': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'crepitacion': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'cuello': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'desviacionaverturadecierre': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dientes': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'difparaAbrirlaboca': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'disminuciondelaavertura': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dolorabertura': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'eCongenitas': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'eDegenerativas': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'eInflamatoriasnotopciones': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'eNeoplasticas': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'encia': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'esquemaCompleto': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'esquemaFalta': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'estudiosdeLaboratorio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ets': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'factorRh': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fatigadolormuscular': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'fechaHospitalizaion': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'fondodesaco': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'frecuenciaCardiaca': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'frecuenciaLavadoDental': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'frecuenciaRespiratoria': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'frenillos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ganglios': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gingivitis': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'glandulassalivales': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gruposanguineo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'habitosHigienicosCorp': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'habitosHigienicosVest': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'habitusExterior': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'herenciaAbuelos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaEsposos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaHermanos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaHijos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaMadre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaPadre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaTios': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicedeplaca': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'interpretacionEstudiosLaboratorio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'interpretacionradiografica': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'istmoBucofaringe': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'labioExterno': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'labiointerno': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lenguaBordes': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lenguaDorso': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lenguaTerciomedio': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lenguaVentral': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Medico']"}),
            'motivo': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'movilidadDentario': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mucosadelBordealveolar': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'musculos': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'otras': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Paciente']"}),
            'padecimientoActual': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'paladarBlando': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'paladarDuro': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'perfil': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'periodontitis': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'peso': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'piel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pisodelaBoca': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'receciongingival': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ruidos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sistemaEndocrina': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sistemaHemopoyetico': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sistemamusculoEsqueletico': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'talla': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'temperatura': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'tensionarterial': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uxiliaresBucales': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'ActividadesClinicas.odontograma': {
            'Meta': {'object_name': 'Odontograma'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Medico']", 'null': 'True'}),
            'fechayHora': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('django.db.models.fields.TextField', [], {}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Paciente']", 'null': 'True'})
        },
        'ActividadesClinicas.procedimiento': {
            'Meta': {'object_name': 'Procedimiento'},
            'cara': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'odontograma': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ActividadesClinicas.Odontograma']", 'null': 'True'}),
            'pieza': ('django.db.models.fields.IntegerField', [], {}),
            'tratamiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ActividadesClinicas.Tratamiento']", 'null': 'True'})
        },
        'ActividadesClinicas.tratamiento': {
            'Meta': {'object_name': 'Tratamiento'},
            'codigoTratamiento': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreTratamiento': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'altas.medico': {
            'Ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Meta': {'object_name': 'Medico'},
            'apellidoMaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'apellidoPaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cedulaEstatal': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'codigoPostal': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'correoElectronico': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'especialidad': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'licenciaDeEspecialidad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'licenciaMedica': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nombreUsuario': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'universidadEgreso': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        'altas.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'apellidoMaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'apellidoPaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'codigoPostal': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'correoElectronico': ('django.db.models.fields.EmailField', [], {'max_length': '60'}),
            'credencialPaciente': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precios.GrupoPrecios']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nSs': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'precios.grupoprecios': {
            'Meta': {'object_name': 'GrupoPrecios'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreDelGrupo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['ActividadesClinicas']