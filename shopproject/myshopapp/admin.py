from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Client, Product, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'location']
    list_filter = ['is_active']
    readonly_fields = ['registration_date']
    actions = ['make_inactive']

    @admin.action(description="Block client")
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)


class ProductPriceListFilter(admin.SimpleListFilter):
    title = _("Цена")
    parameter_name = "price"

    def lookups(self, request, model_admin):
        return [
            ("low_price", _("до 1000")),
            ("mid_price", _("1000-10000")),
            ("over_price", _("свыше 10000")),
        ]

    def queryset(self, request, queryset):
        if self.value() == "low_price":
            return queryset.filter(
                price__lt=1000
            )
        if self.value() == "mid_price":
            return queryset.filter(
                price__gte=1000,
                price__lte=10000
            )
        if self.value() == "over_price":
            return queryset.filter(
                price__gt=10000
            )


class ProductImageListFilter(admin.SimpleListFilter):
    title = _("Изображение товара")
    parameter_name = "image"

    def lookups(self, request, model_admin):
        return [
            ("yes", _("имеется")),
            ("no", _("отсутствует")),
        ]

    def queryset(self, request, queryset):
        if self.value() == "no":
            return queryset.exclude(
                image__icontains='products'
            )
        if self.value() == "yes":
            return queryset.filter(
                image__icontains='products'
            )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity']
    ordering = ['price', '-quantity']
    list_filter = [ProductPriceListFilter, ProductImageListFilter]
    search_fields = ['title']
    search_help_text = 'Поиск товара'
    readonly_fields = ['entry_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Описание',
            {
                'classes': ['collapse'],
                'description': 'Описание товара',
                'fields': ['description', 'image'],
            },
        ),
        (
            'Учет',
            {
                'fields': ['price', 'quantity'],
            }
        ),
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'amount', 'client']
    ordering = ['amount']
    list_filter = ['order_date']
    readonly_fields = ['order_date', 'amount', 'client', 'products']
