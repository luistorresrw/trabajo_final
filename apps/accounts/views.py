# -*- decoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf 
from apps.accounts.forms import *
from apps.prontuarios.models import Personas
from django.contrib import auth
from datetime import datetime, timedelta, date
from django.conf import settings
from django.core import serializers
import random
from django.contrib.auth import *
from trabajo_final.settings import SECRET_KEY
from hashlib import  md5
from random import randint
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives

def home(request):
	login = LoginForm()
	recpass = RecPassForm()
	mensaje = ""
	if request.method == 'POST':
		login = LoginForm(request.POST)
		if login.is_valid():	
			usuario = login.data['usuario']
			password = login.cleaned_data['password']
			user = auth.authenticate(username = usuario, password = password)
			if user is not None and user.is_active:
				request.session['usuario'] = usuario
				request.session['password'] = password
				return HttpResponseRedirect('accounts/')
			else:
				login = LoginForm()
				mensaje = "Usuario y/o contraseña incorrectos."

	values = {
		'recpass':recpass,
		'login':login,
		'mensaje':mensaje,
	}
	return render_to_response('accounts/login.html', values, context_instance = RequestContext(request))  


def login_ok(request):
	mensaje = ""
	if request.method == 'POST':
		input_pil = request.POST['pil']
		usuario = request.session['usuario']
		password = request.session['password']
		user = auth.authenticate(username = usuario, password = password)
		primer_logueo = user.profile.primer_logueo
		print primer_logueo
		if user is not None and user.is_active: 
			if verificar_matriz(request,input_pil,user):
				if primer_logueo == True:
					form = ChangePassForm()
					request.session['user'] = user.username
					return render_to_response('accounts/change_pass.html', {'form':form,}, context_instance = RequestContext(request))
				else:
					login(request, user)
					return HttpResponseRedirect('../prontuarios/')
			else:
				mensaje = "El código PIL ingresado no es correcto."	
		else:
			return HttpResponseRedirect("/")	
	matriz = matrix()
	request.session['matriz'] = matriz
 	keys = matriz.keys()
	values = matriz.values()
	return render_to_response('accounts/login_ok.html', {'matriz':matriz, 'keys':keys,'values':values,'mensaje':mensaje}, context_instance = RequestContext(request))
	

def matrix():
	alpha = [u'A',u'B',u'C',u'D',u'E',u'F',u'G',u'H',u'I',u'J',u'K',u'L',u'M',u'N',u'Ñ',u'O',u'P',u'Q',u'R',u'S',u'T',u'U',u'V',u'W',u'X',u'Y',u'Z']
	matriz = {
		1:[],
		2:[],
		3:[],
		4:[],
		5:[],
		6:[],
		7:[],
		8:[],
		9:[],
	}
	for k in matriz.keys():
		for x in range(3):
			matriz[k].append(get_value(alpha))
		matriz[k] = u''.join(matriz[k])
	return matriz

def get_value(alpha):
	if len(alpha)==1:
		indice = 0
	else:
		indice = random.randrange(0,len(alpha))
	valor = alpha[indice]
	alpha.remove(valor)
	return valor


"""verificar_matriz es una funcion que recibe como argumentos el request, input_pil (que es el ingreso que hizo el usuario de los indices de la matriz), y el usuario,
	con estos datos determina si el segundo factor de identificacion es valido o no."""

def verificar_matriz(request,input_pil,user):
	if input_pil and input_pil != "":																													#verifico que el ingreso de pil no venga vacio
		matriz = request.session['matriz']																												#recupero la matriz desde la sesion
		pil = user.profile.pil.split()																													#recupero el pil del usuario y lo convierto en array
		grupo1 = matriz[int(input_pil[0])]																												#Obtengo el grupo de caracteres seleccionado con el primer indice
		grupo2 = matriz[int(input_pil[1])]																												#Obtengo el grupo de caracteres seleccionado con el segundo indice
		grupo3 = matriz[int(input_pil[2])]																												#Obtengo el grupo de caracteres seleccionado con el tercer indice
		grupo1 = generar_hash(grupo1[0].encode('utf-8'))+' '+generar_hash(grupo1[1].encode('utf-8'))+' '+generar_hash(grupo1[2].encode('utf-8'))		#Convierto el primer grupo de caracteres en un grupo de hash
		grupo2 = generar_hash(grupo2[0].encode('utf-8'))+' '+generar_hash(grupo2[1].encode('utf-8'))+' '+generar_hash(grupo2[2].encode('utf-8'))		#Convierto el segundo grupo de caracteres en un grupo de hash
		grupo3 = generar_hash(grupo3[0].encode('utf-8'))+' '+generar_hash(grupo3[1].encode('utf-8'))+' '+generar_hash(grupo3[2].encode('utf-8'))		#Convierto el tercer grupo de caracteres en un grupo de hash
		veri1 = pil[0] in grupo1																														#verifico si el primer hash del pil esta contenido en el primer grupo hash
		veri2 = pil[1] in grupo2																														#verifico si el segundo hash del pil esta contenido en el segundo grupo hash
		veri3 = pil[2] in grupo3																														#verifico si el tercer hash del pil esta contenido en el tercer grupo hash
		return veri1 and veri2 and veri3																												#devuelvo el valor de verdad de la verificacion.
	return False																																		#devuelvo falso si input_pil es nulo o vacio.
	
def change_password(request):
	if request.method == 'POST':
		form = ChangePassForm(request.POST)
		if form.is_valid():
			username = request.user
			password = form.data['password_actual']
			user = auth.authenticate(username=username, password=password)
			#agregar mensaje
			if user is None:
				return HttpResponseRedirect(reverse('home'))
			else:
				nuevo_password = form.cleaned_data['nuevo_password']
				user.set_password(nuevo_password)
				try:
					user.save()
					profile = user.profile
					profile.primer_logueo = False
					profile.fecha_ultimo_cambio = date.today()
					profile.save()
				except Exception, e:
					raise e
				login(request, user)	
				return HttpResponseRedirect('../../prontuarios/')
	return HttpResponseRedirect(reverse('home'))



def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))



class AutoLogout:
	def process_request(self, request):
		if not request.user.is_authenticated():
			return 
		try:
			ahora = datetime.now()
			if datetime.now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 3000, 0):
				auth.logout(request) 
				
				del request.session['last_touch'] 
				
				
		except KeyError:
			pass
		request.session['last_touch'] = datetime.now()
	

def usuarios(request):
	clase = "user"
	titulo = "Usuarios"
	columns = ["Usuario","Nombre","Email","Fecha Alta","Ultimo Ingreso"]
	usuarios = User()
	form = UserForm()
	if request.method == 'POST':
		password = User.objects.make_random_password(length=10)
		form = UserForm(request.POST)
		print form.is_valid()
		if form.is_valid():
			usuarios.username = form.cleaned_data['username']
			usuarios.first_name = form.cleaned_data['first_name']
			usuarios.last_name = form.cleaned_data['last_name']
			usuarios.is_staff = form.cleaned_data['is_staff']
			usuarios.email = form.cleaned_data['email']
			usuarios.set_password(password)
			try:
				usuarios.save()
				profile = usuarios.get_profile()	
				pil,pil_hashed = generar_pil()
				profile.pil  = pil_hashed
				profile.factor_vencimiento = randint(90,180)
				profile.save()

				info_enviado= True
				subject, from_email, to = 'Asunto : Usuario y Password' ,'divsistemasjp@policia.chubut.gov.ar',usuarios.email
				text_content = ("Hola %s: <br> Le damos la bienvenida al Sistema de Prontuario Policial sus credenciales de acceso son las siguientes:<br> Usuario: %s <br> Password: %s <br> PIL: %s <br>  <strong>Puede acceder haciendo click </strong> <a href='127.0.0.1:8000/spid/'>aqui</a>.<br>Por cualquier consulta y/o reclamos al:\n\n\n<br> email: luistorresrw@gmail.com.-"% (usuarios.first_name,usuarios.username,password,pil))

				msg = EmailMultiAlternatives(subject,text_content,from_email, [to])
				msg.attach_alternative(text_content,'text/html')

				try:
					msg.send(fail_silently=False)
					msg="Se enviaron las credenciales de ingreso al usuario."
				except Exception, e:
					msg="Error al Enviar el correo: "+e	

			except Exception, e:
				raise e
			

			
	lista = User.objects.all()
	tbody = {}
	for elemento in lista:
		tbody[elemento.id] = '<td>'+elemento.username+'</td><td>'+elemento.last_name+', '+elemento.first_name+'</td><td>'+elemento.email+'</td><td>'+elemento.date_joined.strftime('%d/%m/%Y')+'</td><td>'+elemento.last_login.strftime('%d/%m/%Y')+'</td>'
  	return render_to_response('accounts/usuarios.html',{'form':form,'lista':lista, 'titulo':titulo ,'clase':clase,'columns':columns,'tbody':tbody,'usuarios':usuarios},context_instance=RequestContext(request))


def edit_usuarios(request,id):
	pass



def remove_usuarios(request,id):
	pass

def obtener_persona(request,dni):
	data = request.POST
  	persona = Personas.objects.filter(nro_doc = dni)[:1]
  	data = serializers.serialize("json", persona)
  	return HttpResponse(data, mimetype='application/json')



def generar_hash(cadena):
	palabra = cadena+SECRET_KEY
	return md5(str(palabra)).hexdigest()


def generar_pil():
	alpha = [u'A',u'B',u'C',u'D',u'E',u'F',u'G',u'H',u'I',u'J',u'K',u'L',u'M',u'N',u'Ñ',u'O',u'P',u'Q',u'R',u'S',u'T',u'U',u'V',u'W',u'X',u'Y',u'Z']
	pil = get_value(alpha).encode('utf-8')+get_value(alpha).encode('utf-8')+get_value(alpha).encode('utf-8')
	pil_hashed = generar_hash(pil[0])+' '+generar_hash(pil[1])+' '+generar_hash(pil[2])
	return pil,pil_hashed