from django.contrib import admin
from .models import Category, AnimalType, Product, Review, Subscription, ShopContact, ProductImage, ContactRequest

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_discounted', 'price', 'discount_price', 'available', 'created_at', 'updated_at')
    list_editable = ('is_discounted', 'price', 'discount_price', 'available')
    list_filter = ('category', 'animal_types', 'is_discounted', 'available', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('animal_types',)
    autocomplete_fields = ['category']
    inlines = [ProductImageInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'is_visible', 'created_at', 'updated_at')
    search_fields = ('client_name', 'review_text')
    list_filter = ('created_at', 'updated_at', 'is_visible')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    list_filter = ('created_at',)

@admin.register(ShopContact)
class ShopContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address', 'work_hours', 'twitter', 'facebook', 'created_at', 'updated_at')
    search_fields = ('email', 'phone', 'address', 'twitter', 'facebook')
    list_filter = ('created_at', 'updated_at')

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
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
