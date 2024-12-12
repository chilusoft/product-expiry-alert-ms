from django.shortcuts import render

from products.models import Product
from products.forms import ProductForm

# Create your views here.

def index(request):
    all_products = Product.objects.all().order_by('-id')

    ctx = {
        'products': all_products,
        'create_product_form':ProductForm
    }
    return render(request,'index/index.html', ctx)
