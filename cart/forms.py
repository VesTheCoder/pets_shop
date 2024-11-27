from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    '''
    Form for adding products to the cart.
    '''
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CheckoutForm(forms.Form):
    '''
    Form for collecting customer information during checkout.
    '''
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    company = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField(required=False)
    country = forms.CharField(max_length=80)
    address_line_1 = forms.CharField(max_length=255)
    address_line_2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=20)
    order_notes = forms.CharField(widget=forms.Textarea, required=False)