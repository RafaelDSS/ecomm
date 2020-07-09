from django import forms

from products.models import Product


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ProductModelForm(BaseForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category"]
