from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'family_name': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'readonly': True,
                }),
        }
        fields = ('first_name', 'family_name', 'telephone_number', 'delivery_address', 'amount',)
