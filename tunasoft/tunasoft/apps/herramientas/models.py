from django.db import models

# Create your models here.
class herramienta(models.Model):
	nombre	= models.CharField(max_length=50)
	url		= models.URLField()
	status	= models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre

class calendario(models.Model):
	nombre		=models.CharField(max_length=70)

	def __unicode__(self):
		return self.nombre

class proyecto(models.Model):
	nombre		= models.CharField(max_length=70)
	cliente		= models.CharField(max_length=50)
	status		= models.BooleanField(default=True)
	fecha		= models.DateField()
	calendario	= models.ForeignKey(calendario)
	herramientas= models.ManyToManyField(herramienta)

	def __unicode__(self):
		return self.nombre