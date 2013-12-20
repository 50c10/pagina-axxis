# Create your views here.
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from tunasoft.apps.herramientas.models import herramienta, proyecto
from tunasoft.apps.home.models import UserProfile
from tunasoft.apps.herramientas.forms import PresupuestoForm

@login_required(login_url='/login/')
def listado_view(request):	
	herramientas = herramienta.objects.filter(status=True)
	ctx = {'herramientas':herramientas}
	return render_to_response('herramientas/listado.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def calendario_view(request):
	return render_to_response('herramientas/calendario.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def miembros_view(request):
	return render_to_response('herramientas/miembros.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def dashboard_view(request):
	proyectos = proyecto.objects.filter(userprofile__user=request.user)
	ctx = {'proyectos':proyectos}
	return render_to_response('herramientas/dashboard.html',ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def preferences_view(request):
	return render_to_response('herramientas/preferences.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def presupuestos_view(request):
	return render_to_response('herramientas/presupuestos.html', context_instance=RequestContext(request))

def presupuestos2_view(request):
	mensaje = 'nada'
	if request.POST:
		form = PresupuestoForm(request.POST)
		if form.is_valid():
			dias = form.cleaned_data['diaslabsemanales']
			if request.is_ajax():
				mensaje = 'ajax'
				return render(request,'herramientas/presupuestos-resultado.html',{'mensaje':mensaje})
			else:
				mensaje = 'no ajax'
				return render(request,'herramientas/presupuestos-resultado.html',{'mensaje':mensaje})
				#return redirect('presupuestos_success')
		else:
			mensaje = 'Error Forma invalida'
	else:
		form = PresupuestoForm()

	return render(request, 'herramientas/presupuestos-resultado.html',{'form':form,'mensaje':mensaje})