from django import forms
from shop.models import Shop
	
class New_Shop_Form(forms.ModelForm):

	class Meta:
		model = Shop
		fields = ('shop_name',)  