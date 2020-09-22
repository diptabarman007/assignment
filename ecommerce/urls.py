from django.urls import path

from .import views

urlpatterns = [
	path("",views.index, name= 'index'),
	path("productView/<int:myid>",views.productView, name= 'productView'),
	path("about/",views.about, name= 'about'),
	path("contact/",views.contact, name= 'contact'),
	path("largeView/<int:myid>/<i>",views.largeView, name= 'largeView'),
]