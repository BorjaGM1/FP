from django import forms


class OrderForm(forms.Form):
    id = forms.IntegerField(label='id')
    quantity = forms.IntegerField(label='quantity')
