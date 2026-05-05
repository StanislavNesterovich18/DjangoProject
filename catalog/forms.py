from django.forms import ModelForm

from catalog.models import Product
from config.settings import BAN_WORDS


class ProductFormModeration(ModelForm):
    class Meta:
        model = Product
        fields = "name", "description", "price", "image", "category", "is_publish"

    def __init__(self, *args, **kwargs):
        super(ProductFormModeration, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название"})
        self.fields["description"].widget.attrs.update({"class": "form-control", "placeholder": "Введите описание"})
        self.fields["price"].widget.attrs.update({"class": "form-control", "placeholder": "Введите цену"})
        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
        self.fields["category"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
        self.fields["is_publish"].widget.attrs.update({"class": "form-control", "type": "checkbox"})


class ProductForm(ModelForm):
    """Костамизация/стилизация формы и валидация полей"""

    class Meta:
        model = Product
        fields = "name", "description", "price", "image", "category"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название"})
        self.fields["description"].widget.attrs.update({"class": "form-control", "placeholder": "Введите описание"})
        self.fields["price"].widget.attrs.update({"class": "form-control", "placeholder": "Введите цену"})
        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
        self.fields["category"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            self.add_error("price", "Значение должно быть больше нуля")
        return price

    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        for ban in BAN_WORDS:
            if ban in name:
                self.add_error("name", f"Поле содержит запрещеное слово {ban}")
            elif ban in description:
                self.add_error("description", f"Поле содержит запрещеное слово {ban}")
