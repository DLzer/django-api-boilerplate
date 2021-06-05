from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Product

# Create your views here.
def index(request):
    latest_product = Product.objects.order_by('-pub_date')[:5]
    context = {'latest_product': latest_product}
    return render(request, 'products/index.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})

def products_json(request):
    return JsonResponse(list(Product.objects.all().values()), safe=False)

def product_details_json(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        'id': product.id,
        'name': product.product_name,
        'description': product.product_description,
        'published': product.pub_date
    }
    return JsonResponse(context, safe=False)