from django.db import models

class Shop(models.Model):
	shop_name = models.CharField(max_length = 200)
	def __str__(self):
		return self.shop_name


class Book(models.Model):
	on_delete = models.DO_NOTHING
	book_name = models.CharField(max_length = 200)
	book_info = models.TextField()
	knizn = models.ForeignKey(Shop, on_delete = models.PROTECT)

# Create your models here.
