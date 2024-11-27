from django.db import models

class Category(models.Model):
    '''
    Represents a category for products.
    '''
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class AnimalType(models.Model):
    '''
    Represents a type of animal associated with products.
    '''
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    '''
    Represents a product in the shop.
    '''
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    animal_types = models.ManyToManyField(AnimalType, related_name='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_discounted = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_discounted_price(self):
        '''
        Returns the discounted price if applicable, otherwise returns the regular price.
        '''
        if self.is_discounted and self.discount_price:
            return self.discount_price
        return self.price
    
    def get_absolute_url(self):
        '''
        Returns the absolute URL for the product.
        '''
        return f'/products/{self.category.slug}/{self.slug}/'

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    '''
    Represents an image associated with a product.
    '''
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f'Image for {self.product.name}'
    
class Review(models.Model):
    '''
    Represents a customer review.
    '''
    client_name = models.CharField(max_length=100)
    client_photo = models.ImageField(upload_to='reviews/', blank=True, null=True)
    review_text = models.TextField()
    is_visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.client_name}'

class Subscription(models.Model):
    '''
    Represents a user's subscription to the shop's mailing list.
    '''
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class ShopContact(models.Model):
    '''
    Represents contact information for the shop.
    '''
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    work_hours = models.TextField(default='24/7')
    twitter = models.URLField(blank=True, null=True, default=None)
    facebook = models.URLField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
class ContactRequest(models.Model):
    '''
    Represents a contact request from a user.
    '''
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contact Request from {self.name} - {self.email}'