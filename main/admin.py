from django.contrib import admin
from .models import (
    Category, AnimalType, Product, Review, Subscription, 
    ShopContact, ProductImage, ContactRequest, Currency
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the Category model.
    '''
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the AnimalType model.
    '''
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

class ProductImageInline(admin.TabularInline):
    '''
    Inline admin for ProductImage model to be used in ProductAdmin.
    '''
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the Product model.
    '''
    list_display = ('name', 'category', 'is_discounted', 'price', 'currency', 'discount_price', 'available', 'created_at', 'updated_at')
    list_editable = ('is_discounted', 'price', 'discount_price', 'available', 'currency')
    list_filter = ('category', 'animal_types', 'is_discounted', 'available', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('animal_types',)
    autocomplete_fields = ['category', 'currency']
    inlines = [ProductImageInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the Review model.
    '''
    list_display = ('client_name', 'is_visible', 'created_at', 'updated_at')
    search_fields = ('client_name', 'review_text')
    list_filter = ('created_at', 'updated_at', 'is_visible')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the Subscription model.
    '''
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    list_filter = ('created_at',)

@admin.register(ShopContact)
class ShopContactAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the ShopContact model.
    '''
    list_display = ('email', 'phone', 'address', 'work_hours', 'twitter', 'facebook', 'created_at', 'updated_at')
    search_fields = ('email', 'phone', 'address', 'twitter', 'facebook')
    list_filter = ('created_at', 'updated_at')

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the ContactRequest model.
    '''
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Timestamp', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the Currency model.
    '''
    list_display = ('code', 'symbol', 'is_default', 'created_at', 'updated_at')
    list_editable = ('is_default',)
    search_fields = ('code', 'symbol')
    list_filter = ('is_default', 'created_at', 'updated_at')
    ordering = ('-is_default', 'code')
