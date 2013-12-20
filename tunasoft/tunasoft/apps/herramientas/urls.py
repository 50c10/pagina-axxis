from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('tunasoft.apps.herramientas.views',
	url(r'^listado/$','listado_view',name='vista_Listado'),
	url(r'^dashboard/$','dashboard_view',name='dashboard_view'),
	url(r'^preferences/$','preferences_view',name='preferences_view'),
	url(r'^calendario/$','calendario_view',name='calendario_view'),
	url(r'^miembros/$','miembros_view',name='miembros_view'),
	url(r'^presupuestos/$','presupuestos_view',name='presupuestos_view'),
	url(r'^presupuestos/success/$', TemplateView.as_view(template_name='herramientas/presupuestos.html'),name="presupuestos_success"),
)