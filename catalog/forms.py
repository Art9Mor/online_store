from django import forms

from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user', 'is_active', 'is_published')

    censored = ['казино',
                'криптовалюта',
                'крипта',
                'биржа',
                'дешево',
                'бесплатно',
                'обман',
                'полиция',
                'радар'
                ]

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in self.censored:
            if word in cleaned_data:
                raise forms.ValidationError('Недопустимое слово!')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in self.censored:
            if word in cleaned_data:
                raise forms.ValidationError(f'Недопустимое слово - {word}!')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ModeratorProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')
