# Create your views here.
from django.contrib.auth import logout , authenticate ,login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from tunasoft.apps.home.forms import LoginForm ,ContactoForm
from django.core.mail import EmailMultiAlternatives
from tunasoft.apps.home.models import UserProfile
from tunasoft.apps.home.models import contacto
def index_view(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

def about_view(request):
	return render_to_response('home/about.html', context_instance=RequestContext(request))

def contact_view(request):
	info_enviado = False 
	email =""
	titulo = ""
	texto = ""

	if request.method == "POST":
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

			contact = contacto()
			contact.Email = email
			contact.Titulo = titulo
			contact.Texto = texto
			contact.save()
			# COnfiguraciond de envio de correo

			#to_admin = 'pako50c10@gmail.com'
			#html_content = "Informacion recibida <br><br><br>Mensaje<br><br><br>%s"%(texto)
			#msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			#msg.attach_alternative(html_content,'text/html')
			#msg.send()
	else:
		formulario = ContactoForm()
	ctx = {'form':formulario, 'email':email, 'titulo':titulo, 'texto':texto, 'info_enviado':info_enviado}
	return render_to_response('home/contact.html',ctx, context_instance=RequestContext(request))

def web_view(request):
	return render_to_response('home/web.html', context_instance=RequestContext(request))

def sistemas_view(request):
	return render_to_response('home/sistemas.html', context_instance=RequestContext(request))

def movil_view(request):
	return render_to_response('home/movil.html', context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/dashboard')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/dashboard')
				else:
					mensaje = "usuario o password incorrecto"
		form = LoginForm()
		ctx ={'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html', ctx, context_instance=RequestContext(request))

def equipo_view(request):
	usuarios = UserProfile.objects.all()
	ctx = {'usuarios':usuarios}
	return render_to_response('home/equipo.html',ctx,context_instance=RequestContext(request))

def instalaciones_view(request):
	return render_to_response('home/instalaciones.html', context_instance=RequestContext(request))

