#encoding: utf-8
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from Inventario.models import Categoria
from Inventario.models import Producto
from crispy_forms.layout import(Layout,Fieldset,HTML,Field,ButtonHolder,
Submit)

class CategoriaForm(forms.ModelForm):
       class Meta:
               model=Categoria

       def __init__(self, *args, **kwargs):
		super(CategoriaForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML(""" 
							<p> Rellene todos los Campos Con *.</p>

							"""
			),
			Fieldset(
				'Informacion de Rigor',
				
				Field('nombre' , wrapper_class='col-md-8'),		


				),
			ButtonHolder(
					Submit('save','Guardar')
			)
		)		
		self.fields['nombre'].label='Nombre'
		

class ProductoForm(forms.ModelForm):
      class Meta:
             model=Producto


      def __init__(self, *args, **kwargs):
      	super(ProductoForm,self).__init__(*args, **kwargs)
      	self.helper=FormHelper()
      	self.helper=FormHelper()
      	self.helper.layout=Layout(
      		HTML(
      			"""
      					<p>Rellene la Informacion marcada con *.</p>
      					"""
      					),
      		Fieldset(
      			'Informacion de Producto',
      			Field('nombre',wrapper_class='col-md-5'),
      			Field('descripcion',wrapper_class='col-md-5'),
      			Field('precio',wrapper_class='col-md-2'),
      			Field('categoria',wrapper_class='col-md-4'),
      			),
      		ButtonHolder(
      			Submit('save','Registrar')
      			)
      		)
      	self.fields['nombre'].label='Nombre del Producto'
      	self.fields['descripcion'].label='Descripcion'
      	self.fields['precio'].label='Precio'
      	self.fields['categoria'].label='Categoria'

      





