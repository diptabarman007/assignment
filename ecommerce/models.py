from django.db import models

class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	product_name = models.CharField(max_length=50)
	category = models.CharField(max_length=50, default="")
	subcategory = models.CharField(max_length=50, default="")
	price = models.IntegerField(default=0)
	desc = models.CharField(max_length=300)
	pub_date = models.DateField()
	video = models.CharField(max_length=300, default="")
	image1 = models.ImageField(upload_to="ecommerce/images",default="")
	image2 = models.ImageField(upload_to="ecommerce/images",default="")
	image3 = models.ImageField(upload_to="ecommerce/images",default="")

	def __str__(self):
		return self.product_name

class Contact(models.Model):
	msg_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=70, default="")	
	phone = models.IntegerField(default=0)
	desc = models.CharField(max_length=500, default="")
	


	def __str__(self):
		return self.name