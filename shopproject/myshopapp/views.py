from datetime import timedelta, date

from django.shortcuts import render
import logging

from myshopapp.forms import ProductForm
from myshopapp.models import Client, Order, Product

logger = logging.getLogger(__name__)


def log_this(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        logger.info(f'Func "{f.__name__}" was called')
        return res

    return wrapper


@log_this
def index(request):
    return render(request, "myshopapp/index.html")


@log_this
def task3(request):
    return render(request, "myshopapp/task3.html")


@log_this
def task4(request):
    return render(request, "myshopapp/task4.html")


@log_this
def client_orders(request, client_id: int):
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client__pk=client_id)
    content = {"client": client,
               "orders": []}
    for order in orders:
        products = order.products.all()
        content["orders"].append({"date": order.order_date,
                                  "amount": order.amount,
                                  "products": products})
    return render(request, "myshopapp/client_orders.html", content)


@log_this
def client_products(request, client_id: int):
    today = date.today()
    week = today - timedelta(7)
    month = today - timedelta(30)
    year = today - timedelta(365)

    client = Client.objects.filter(pk=client_id).first()

    week_orders = Order.objects.filter(client=client, order_date__gte=week)
    month_orders = Order.objects.filter(client=client, order_date__gte=month)
    year_orders = Order.objects.filter(client=client, order_date__gte=year)

    week_product_list = {product for order in week_orders for product in order.products.all()}
    month_product_list = {product for order in month_orders for product in order.products.all()}
    year_product_list = {product for order in year_orders for product in order.products.all()}

    content = {"client": client,
               "week_product_list": week_product_list,
               "month_product_list": month_product_list,
               "year_product_list": year_product_list}

    return render(request, "myshopapp/client_products.html", content)


@log_this
def product_add(request):
    result = False
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            product = Product(title=title,
                              description=description,
                              price=price,
                              quantity=quantity,
                              image=image)
            product.save()
            result = True
    else:
        result = False
        form = ProductForm()
    return render(request, 'myshopapp/product_add.html',
                  {'form': form, 'result': result})


@log_this
def product_change(request, product_id: int):
    result = False
    product = Product.objects.filter(pk=product_id).first()
    product_img = None
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            result = True
            product.title = form.cleaned_data['title']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            if form.cleaned_data['image'] is not None:
                product.image = form.cleaned_data['image']
            product.save()
    else:
        result = False
        if product:
            data = {'title': product.title,
                    'description': product.description,
                    'price': product.price,
                    'quantity': product.quantity}
            if product.image is not None:
                product_img = product.image
            form = ProductForm(data)
        else:
            form = ProductForm()
    return render(request, 'myshopapp/product_change.html',
                  {'form': form,
                   'result': result,
                   'product_img': product_img,
                   'product': product})
