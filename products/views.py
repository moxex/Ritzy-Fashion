from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Product, Order, OrderItem
from cart.forms import CartAddProductForm
from .forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    related_products = Product.objects.order_by('-category')[:4]
    products = Product.objects.filter(available=True)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'related_products': related_products
    }
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products/products_list.html', context)


def product_detail(request, id, slug):
    category = None
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    products = Product.objects.filter(available=True)
    related_products = Product.objects.order_by('-category')[:4]
    cart_product_form = CartAddProductForm()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product,
        'category': category,
        'categories': categories,
        'products' : products,
        'cart_product_form': cart_product_form,
        'related_products': related_products
    }
    return render(request, 'products/product_details.html', context)


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            
            # clear the cart
            # cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            context = {
                'order': order,
                'cart': cart,
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone_number']
            }
            return render(request, 'products/pay_with_paystack.html', context)
    else:
        form = OrderCreateForm()
    return render(request, 'products/create.html', {'cart': cart, 'form': form})


def product_category(request, category, slug):
    product = Product.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-date'
    )
    context = {
        "category": category,
        "product": product,
    }
    return render(request, "products/category_product_list.html", context)
