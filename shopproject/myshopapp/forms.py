from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(max_length=100,
                            label="Наименование товара",
                            widget=forms.TextInput(attrs={'class': 'product-form__title'}))
    description = forms.CharField(max_length=1000,
                                  label="Описание товара",
                                  widget=forms.Textarea(attrs={'class': 'product-form__description'}))
    price = forms.DecimalField(max_digits=8, decimal_places=2, label="Цена")
    quantity = forms.IntegerField(min_value=1, label="Количество")
    image = forms.ImageField(required=False, label="Изображение товара")
