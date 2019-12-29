from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from shop.models import Shop
from shop.forms import New_Shop_Form

def index(request):
    latest_shop_list = Shop.objects.all().order_by('-shop_name')[:5]
    context = {'latest_shop_list': latest_shop_list}
    return render(request, 'shop/index.html', context)

def detail(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'shop/detail.html', {'shop': shop})

def post_new(request):
	if request.method == "POST":
		form = New_Shop_Form(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
	else:
		form = New_Shop_Form()

	return render(request, 'shop/shop_edit.html', {'form': form})



##Добавить форму
