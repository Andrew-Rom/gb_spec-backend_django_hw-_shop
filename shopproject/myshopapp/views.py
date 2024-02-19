from datetime import timedelta, date
from sys import stdout

from django.shortcuts import render
import logging

from myshopapp.models import Client, Order

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

    week_orders = (Order.objects.filter(client__pk=client_id)
                   & Order.objects.filter(order_date__range=(week, today)).order_by("-order_date"))
    month_orders = (Order.objects.filter(client__pk=client_id)
                    & Order.objects.filter(order_date__range=(month, week)).order_by("-order_date"))
    year_orders = (Order.objects.filter(client__pk=client_id)
                   & Order.objects.filter(order_date__range=(year, month)).order_by("-order_date"))

    week_product_list = [product for order in week_orders for product in order.products.all()]
    month_product_list = [product for order in month_orders for product in order.products.all()]
    year_product_list = [product for order in year_orders for product in order.products.all()]

    content = {"client": client,
               "week_product_list": week_product_list,
               "month_product_list": month_product_list,
               "year_product_list": year_product_list}

    return render(request, "myshopapp/client_products.html", content)
