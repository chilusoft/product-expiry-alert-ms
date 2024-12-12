from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import ProductBatch, ProductCategory

class ProductForm(forms.Form):
    name = forms.CharField(label="Product Name", max_length=100)
    image = forms.ImageField(label="Product Image")
    batch_number = forms.ChoiceField(
        label="Batch Number",
        choices=[(f'{b.id}', f'Batch {b.id}') for b in ProductBatch.objects.all()]  # Add your batch numbers
    )
    category = forms.MultipleChoiceField(
        label="Category",
        choices=[(f'{c.id}', f'{c.name.title()}') for c in ProductCategory.objects.all()],  # Add your categories
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = "products/create-product/"
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'name',
            'image',
            'batch_number',
            'category',
            Submit('submit', 'Add Product', css_class='btn-primary')
        )

    