from django.shortcuts import render
from django.http import HttpResponse

from django.contrib import messages

from .models import Contact, Product 

from django.core.mail import send_mail



def index(request):
	allProds = Product.objects.all()

	params = {'allProds': allProds}
	return render(request, 'ecommerce/index.html', params )


def productView(request, myid):

	product = Product.objects.filter(product_id = myid)
	
	return render(request, 'ecommerce/productView.html', {'product': product[0]})

def about(request):
	
	return render(request, 'ecommerce/about.html')

def contact(request):
	if request.method == "POST":
		name = request.POST.get('name','')
		email = request.POST.get('email','')
		phone = request.POST.get('phone','')
		desc = request.POST.get('desc','')
		contact = Contact(name=name, email=email, phone=phone, desc=desc)
		contact.save()

		messages.success(request,"your grievences has been successfully forwarded")
		#sending email..



		'''send_mail(
			"message from "+ name, #subject
			desc, #message
			email, #from email
			['dypta23barman@gmail.com'], #to Email
			fail_silently= False,
			)
		
			'''
		return render(request, 'ecommerce/contact.html',{'name':name})
		
		
	else:
		return render(request, 'ecommerce/contact.html')

	
		
def largeView(request, myid, i):

	product = Product.objects.filter(product_id = myid)
	
	return render(request, 'ecommerce/largeView.html', {'product': product[0]}, {'i':i})
