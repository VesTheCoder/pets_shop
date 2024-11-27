from decimal import Decimal
from django.conf import settings
from main.models import Product


class Cart(object):
    '''
    A class representing a shopping cart.
    
    This cart is stored in the session and persists for the duration of the user's session.
    '''

    def __init__(self, request):
        '''
        Initialize the cart.

        Args:
            request: The current request object.
        '''
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        '''
        Add a product to the cart or update its quantity.

        Args:
            product: The product to add to the cart.
            quantity: The quantity of the product to add.
            override_quantity: If True, set the quantity instead of adding to it.
        '''
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0, 
                'price': str(product.get_discounted_price())
            }
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        '''
        Save the cart to the session.
        '''
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        '''
        Remove a product from the cart.

        Args:
            product: The product to remove from the cart.
        '''
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        '''
        Iterate over the items in the cart and get the products from the database.

        Yields:
            A dictionary for each item in the cart with product and price information.
        '''
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product
            cart[str(product.id)]['price'] = Decimal(product.get_discounted_price())
        
        for item in cart.values():
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        '''
        Get the total number of items in the cart.

        Returns:
            The total quantity of all items in the cart.
        '''
        return sum(item['quantity'] for item in self.cart.values())
    
    def clear(self):
        '''
        Remove the cart from session.
        '''
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_price(self):
        '''
        Calculate the total price of all items in the cart.

        Returns:
            The total price of all items in the cart.
        '''
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())