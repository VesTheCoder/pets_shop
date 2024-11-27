from django.test import TestCase
from cart.forms import CartAddProductForm, CheckoutForm
from django.contrib.auth.models import User
from decimal import Decimal
from .models import Order

class CartAddProductFormTest(TestCase):
    '''
    Tests for CartAddProductForm validation.
    '''

    def test_valid_quantity(self):
        '''
        Test form with a valid quantity.
        '''
        form = CartAddProductForm(data={'quantity': 5, 'override': False})
        self.assertTrue(form.is_valid())

    def test_invalid_quantity(self):
        '''
        Test form with an invalid quantity.
        '''
        form = CartAddProductForm(data={'quantity': 25, 'override': False})
        self.assertFalse(form.is_valid())

class CheckoutFormTest(TestCase):
    '''
    Tests for CheckoutForm validation.
    '''

    def test_valid_checkout_form(self):
        '''
        Test form with valid data.
        '''
        form = CheckoutForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'email': 'john.doe@example.com',
            'country': 'USA',
            'address_line_1': '123 Main St',
            'city': 'New York',
            'zip_code': '10001',
            'order_notes': '',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_checkout_form(self):
        '''
        Test form with missing required fields.
        '''
        form = CheckoutForm(data={'first_name': ''})
        self.assertFalse(form.is_valid())

class OrderModelTest(TestCase):
    '''
    Test case for the Order model.
    '''

    def setUp(self):
        '''
        Set up test data for Order model tests.
        '''
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.order_data = {
            'user': self.user,
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '+1234567890',
            'email': 'john.doe@example.com',
            'country': 'United States',
            'address_line_1': '123 Test Street',
            'city': 'Test City',
            'zip_code': '12345',
            'items': {'item1': {'quantity': 2, 'price': 10.99}},
            'subtotal': Decimal('64.98'),
            'shipping_cost': Decimal('5.02'),
            'total': Decimal('69.00'),
        }

    def test_create_order(self):
        '''
        Test creating an order and verifying its attributes.
        '''
        order = Order.objects.create(**self.order_data)
        self.assertEqual(order.first_name, 'John')
        self.assertEqual(order.last_name, 'Doe')
        self.assertEqual(order.status, 'new')  # Check default status
        self.assertEqual(order.total, Decimal('69.00'))

    def test_order_str_representation_with_user(self):
        '''
        Test the string representation of an order with a user.
        '''
        order = Order.objects.create(**self.order_data)
        expected_str = f'Order {order.id} by test@example.com - Status: new'
        self.assertEqual(str(order), expected_str)

    def test_order_str_representation_without_user(self):
        '''
        Test the string representation of an order without a user.
        '''
        self.order_data['user'] = None
        order = Order.objects.create(**self.order_data)
        expected_str = f'Order {order.id} by Guest - Status: new'
        self.assertEqual(str(order), expected_str)

    def test_optional_fields(self):
        '''
        Test that optional fields can be blank.
        '''
        order_data = self.order_data.copy()
        order_data.update({
            'company': '',
            'email': '',
            'address_line_2': '',
            'order_notes': ''
        })
        order = Order.objects.create(**order_data)
        self.assertEqual(order.company, '')
        self.assertEqual(order.email, '')
        self.assertEqual(order.address_line_2, '')
        self.assertEqual(order.order_notes, '')

    def test_status_choices(self):
        '''
        Test all possible status transitions for an order.
        '''
        order = Order.objects.create(**self.order_data)
        
        valid_statuses = ['new', 'processed', 'shipped', 'delivered', 'canceled']
        for status in valid_statuses:
            order.status = status
            order.save()
            self.assertEqual(order.status, status)

    def test_decimal_fields_precision(self):
        '''
        Test the precision of decimal fields in the Order model.
        '''
        order = Order.objects.create(**self.order_data)
        self.assertEqual(order.subtotal, Decimal('64.98'))
        self.assertEqual(order.shipping_cost, Decimal('5.02'))
        self.assertEqual(order.total, Decimal('69.00'))