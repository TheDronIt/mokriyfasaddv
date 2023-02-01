from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
	path('', views.index__page, name='home'),
	path('service', views.services__page),
	path('service/<int:id>', views.about_services__page),
	path('portfolio', views.portfolios__page),
	path('portfolio/<int:id>', views.about_portfolios__page),
	path('certificate', views.certificate__page),
	path('contacts', views.contacts__page),
	path('privacy', views.privacy__page),
	]