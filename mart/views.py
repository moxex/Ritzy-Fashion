from itertools import product
from multiprocessing import context
from django.shortcuts import render
from django.db.models import Q
from django.views import View
from products.models import Product, Category

# Create your views here.
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-id')[:8]
    latest_products = Product.objects.order_by('-category')[:4]
    context = {
        'categories': categories,
        'products': products,
        'latest_products': latest_products,

    }
    return render(request, 'mart/index.html', context)