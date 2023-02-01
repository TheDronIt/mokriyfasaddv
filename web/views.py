from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import *


def index__page(request):
	category = Category.objects.filter(Visibility="Отображать")
	data = {
		"Categorys": category
	}
	return render(request, 'page/index.html', data)


def services__page(request):
	category = Category.objects.filter(Visibility="Отображать")
	data = {
		"Categorys": category
	}
	return render(request, 'page/services.html', data)


def about_services__page(request, id):
	service = Service.objects.get(id=id)
	data ={
		"Service": service
	}
	return render(request, 'page/about_services.html', data)


def portfolios__page(request):
	portfolios = Portfolio.objects.filter(Visibility="Отображать")
	data = {
		"Portfolios": portfolios
	}
	return render(request, 'page/portfolios.html', data)


def about_portfolios__page(request, id):
	portfolio = Portfolio.objects.get(id=id)
	data ={
		"Portfolio": portfolio
	}
	return render(request, 'page/about_portfolios.html', data)	


def certificate__page(request):
	certificate = Certificate.objects.filter(Visibility="Отображать")
	data = {
		"Certificates": certificate
	}
	return render(request, 'page/certificate.html', data)


def contacts__page(request):
	jobs = Jobs.objects.all()
	data = {
		"Jobs": jobs
	}
	return render(request, 'page/contacts.html', data)


def privacy__page(request):
	data = {
	}
	return render(request, 'page/privacy.html', data)