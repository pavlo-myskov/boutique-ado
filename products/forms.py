from django import forms

from .models import Product, Category


class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # list of tuples of the id and friendly name
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Update the category field on the form to use friendly names
        self.fields['category'].choices = friendly_names
        # add class to fields to match the theme of the website
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
