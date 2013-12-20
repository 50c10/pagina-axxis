from django.db import models
from django.contrib.auth.models import User
from tunasoft.apps.herramientas.models import proyecto

# Create your models here.
class UserProfile(models.Model):
	def url(self,filename):
		ruta = "Users/%s/%s"%(self.user.username,filename)
		return ruta

	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to=url)
	descripcion = models.TextField(max_length=300)
	proyectos = models.ManyToManyField(proyecto)

	def __unicode__(self):
		return self.user.username

class contacto(models.Model):
	Email = models.EmailField()
	Titulo = models.CharField(max_length=60)
	Texto = models.CharField(max_length=500)