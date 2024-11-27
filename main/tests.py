from django.test import TestCase, Client
from django.urls import reverse
from .models import (
    Category, AnimalType, Product, Review, Subscription, ContactRequest, ShopContact
)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .forms import UserRegistrationForm, LoginForm
from django.core.files.uploadedfile import SimpleUploadedFile



class ModelsTestCase(TestCase):
    '''
    Models Tests
    '''
    def setUp(self):
        self.category = Category.objects.create(name='Category1', slug='category-1')
        self.animal_type = AnimalType.objects.create(name='Dogs', description='For all dog lovers')
        self.product = Product.objects.create(
            name='Dog Food',
            slug='dog-food',
            category=self.category,
            description='Premium dog food',
            price=50.00,
            is_discounted=True,
            discount_price=45.00
        )
        self.subscription = Subscription.objects.create(email='test@example.com')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Category1')

    def test_animal_type_str(self):
        self.assertEqual(str(self.animal_type), 'Dogs')

    def test_product_get_discounted_price(self):
        self.assertEqual(self.product.get_discounted_price(), 45.00)

    def test_subscription_str(self):
        self.assertEqual(str(self.subscription), 'test@example.com')



class UserRegistrationFormTest(TestCase):
    '''
    Forms Tests
    '''
    def test_valid_form(self):
        form_data = {
            'email': 'user@example.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        User.objects.create(email='user@example.com')
        form_data = {
            'email': 'user@example.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], 'This email is already registered.')

    def test_password_mismatch(self):
        form_data = {
            'email': 'user@example.com',
            'password': 'password123',
            'confirm_password': 'differentpassword'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['__all__'][0], "Passwords doesn't match")



class ViewsTestCase(TestCase):
    '''
    Views Tests
    '''
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Category1', slug='category-1')
        self.product = Product.objects.create(
            name='Dog Food',
            slug='dog-food',
            category=self.category,
            description='Premium dog food',
            price=50.00,
            available=True
        )
        self.shop_contact = ShopContact.objects.create(
            phone='123-456-7890',
            email='contact@example.com',
            address='123 Main Street',
            work_hours='24/7'
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index/index.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '123-456-7890')
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dog Food')
        self.assertTemplateUsed(response, 'product_list/product_list.html')

    def test_single_product_view(self):
        response = self.client.get(reverse('single-product', args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dog Food')
        self.assertTemplateUsed(response, 'single-product/single-product.html')



class UserInteractionTest(TestCase):
    '''
    Subscriptions and Orders Tests
    '''
    def setUp(self):
        self.client = Client()

    def test_subscribe_success(self):
        response = self.client.post(reverse('subscribe'), {'email': 'newuser@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thank you for your subscription!')
        self.assertTrue(Subscription.objects.filter(email='newuser@example.com').exists())

    def test_subscribe_duplicate_email(self):
        Subscription.objects.create(email='duplicate@example.com')
        response = self.client.post(reverse('subscribe'), {'email': 'duplicate@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thank you, you are already subscribed')

    def test_contact_request_success(self):
        response = self.client.post(reverse('contact_request'), {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Hello',
            'message': 'Test message'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thanks for reaching out! We will get back to you soon.')
        self.assertTrue(ContactRequest.objects.filter(email='johndoe@example.com').exists())

    def test_contact_request_missing_field(self):
        response = self.client.post(reverse('contact_request'), {
            'name': '', 
            'email': 'johndoe@example.com',
            'subject': 'Hello',
            'message': 'Test message'
        })
        self.assertEqual(response.status_code, 400) 
        self.assertJSONEqual(
            response.content.decode('utf-8'),
            {"success": False, "message": "All fields are required."}
        )



class ContextProcessorTest(TestCase):
    '''
    Context Processors Tests
    '''
    def setUp(self):
        self.shop_contact = ShopContact.objects.create(
            phone='123-456-7890',
            email='contact@example.com',
            address='123 Main Street',
            work_hours='24/7'
        )

    def test_shop_contact_context(self):
        response = self.client.get(reverse('index'))
        self.assertIn('shop_contact', response.context)
        self.assertEqual(response.context['shop_contact'].email, 'contact@example.com')
