from django.contrib import admin
from .models import Category, AnimalType, Product, Review, Cart, CartItem, Order, OrderItem, Subscription, ShopContact

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name')}
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name')
    list_filter = ('created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_discounted', 'price', 'discount_price', 'available', 'created_at', 'updated_at')
    list_editable = ('is_discounted', 'price', 'discount_price', 'available')
    list_filter = ('category', 'animal_types', 'is_discounted', 'available', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name')}
    filter_horizontal = ('animal_types')
    autocomplete_fields = ['category']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'is_visible', 'created_at', 'updated_at')
    search_fields = ('client_name', 'review_text')
    list_filter = ('created_at', 'updated_at', 'is_visible')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username')
    list_filter = ('created_at')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    list_editable = ('quantity')
    search_fields = ('cart__user__username', 'product__name')
    autocomplete_fields = ['cart', 'product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'status', 'created_at')
    list_editable = ('status',)
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'created_at')
    autocomplete_fields = ['user']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    list_editable = ('quantity', 'price')
    search_fields = ('order__user__username', 'product__name')
    autocomplete_fields = ['order', 'product']

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email')
    list_filter = ('created_at')

@admin.register(ShopContact)
class ShopContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address', 'created_at', 'updated_at')
    search_fields = ('email', 'phone', 'address')
    list_filter = ('created_at', 'updated_at')
