import uuid

from django.template.context import RequestContext
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User

from apps.hemeroteca.models import Articulo, Revista
from .models import Libro, Carrera, Estudiante, Reserva

from apps.userprofile.form import EmailAuthenticationForm
# Create your views here.

def home(request):
	carreras  = Carrera.objects.all()
	libros	  = Libro.objects.order_by("-id").all()[:10]
	revistas  = Revista.objects.order_by("-id").all()[:4]
	articulos = Articulo.objects.order_by("-id").all()[:4]

	formAuth  = EmailAuthenticationForm(request.POST or None)

	if formAuth.is_valid():
		login(request, formAuth.get_user())

	template = 'index.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))


def biblioteca(request):
	carreras  = Carrera.objects.all()
	libros_list	  = Libro.objects.order_by("-id").all()

	paginator = Paginator(libros_list, 1) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		libros = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		libros = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		libros = paginator.page(paginator.num_pages)

	template = 'biblioteca.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))


def biblioteca_carrera(request, id_carrera):
	carreras  = Carrera.objects.all()
	carrera   = Carrera.objects.get(id = id_carrera)
	libros_list	  = Libro.objects.filter(carrera = carrera)

	paginator = Paginator(libros_list, 1) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		libros = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		libros = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		libros = paginator.page(paginator.num_pages)

	template = 'biblioteca.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))


def hemeroteca(request):
	revistas  = Revista.objects.order_by("-id").all()
	articulos = Articulo.objects.order_by("-id").all()

	formAuth  = EmailAuthenticationForm(request.POST or None)

	if formAuth.is_valid():
		login(request, formAuth.get_user())

	template = 'hemeroteca.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))


def book_detail_view(request, id_book, id_user):
	libro = get_object_or_404(Libro, id = id_book)
	estudent  = Estudiante.objects.get(id = id_user)

	formAuth  = EmailAuthenticationForm(request.POST or None)

	if formAuth.is_valid():
		login(request, formAuth.get_user())

	template = 'detail-book.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))


def reserva(request, id_book, id_user):
	libro  = Libro.objects.get(id = id_book)
	estudent = Estudiante.objects.get(id = id_user)
	usuario = User.objects.get(id = id_user)



	def my_random_string(string_length=10):
	    """Returns a random string of length string_length."""
	    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
	    random = random.upper() # Make all characters uppercase.
	    random = random.replace("-","") # Remove the UUID '-'.
	    codigo = random[0:string_length]
	    return codigo # Return the random string.

	codres = my_random_string(6)
	res = Reserva()
	res.reserva = codres
	res.libro = libro
	res.estudiante = estudent
	res.save()
	reserva = Reserva.objects.get(reserva = codres)

	estudent.reservas = True
	estudent.save()

	libro.stockChange = libro.stockChange - 1
	if libro.stockChange == 0:
		libro.estado = False

	libro.save()


	template = 'detail-book.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))


def LogOut(request):
	logout(request)

	return redirect('/')