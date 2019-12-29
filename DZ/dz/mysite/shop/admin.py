from django.contrib import admin
from shop.models import Shop, Book

class Book_in_line(admin.TabularInline):
	model = Book
	extra = 3

class ShopAdmin(admin.ModelAdmin):
	fields = ['shop_name']

	inlines = [Book_in_line]

admin.site.register(Shop, ShopAdmin)
# Register your models here.
