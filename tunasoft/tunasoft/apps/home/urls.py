from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tunasoft.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^contact/$','contact_view',name='vista_contact'),
	url(r'^web/$','web_view',name='web_view'),
	url(r'^sistemas/$','sistemas_view',name='sistemas_view'),
	url(r'^movil/$','movil_view',name='movil_view'),
	url(r'^equipo/$','equipo_view',name='equipo_view'),
	url(r'^instalaciones/$','instalaciones_view',name='instalaciones_view'),


	# Login/logout URLS
	url(r'^login/$','login_view',name='login_view'),
    url(r'^logout/$','logout_view',name='logout_view'),
)