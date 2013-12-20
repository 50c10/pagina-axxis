from django.contrib	import admin
from tunasoft.apps.herramientas.models import herramienta, proyecto, calendario

admin.site.register(herramienta)
admin.site.register(proyecto)
admin.site.register(calendario)