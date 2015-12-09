from django.template.context import RequestContext
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.hemeroteca.models import Articulo, Revista
from .models import Libro, Carrera
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
	libros	  = Libro.objects.order_by("-id").all()[:10]
	
	formAuth  = EmailAuthenticationForm(request.POST or None)

	paginator = Paginator(libros, 1)

	page = request.GET.get('page')

	try:
		libro = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		libro = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		libro = paginator.page(paginator.num_pages)

	if formAuth.is_valid():
		login(request, formAuth.get_user())

	template = 'biblioteca.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))


def biblioteca_carrera(request, id_carrera):
	carreras  = Carrera.objects.all()
	carrera   = Carrera.objects.get(id = id_carrera)
	libros	  = Libro.objects.filter(carrera = carrera)

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


def book_detail_view(request, id):

	libro = get_object_or_404(Libro, id = id)

	formAuth  = EmailAuthenticationForm(request.POST or None)

	if formAuth.is_valid():
		login(request, formAuth.get_user())

	template = 'detail-book.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))


def LogOut(request):
	logout(request)

	return redirect('/')