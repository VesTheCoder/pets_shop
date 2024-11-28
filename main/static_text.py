
def email_sub_static_text(request):
    '''
    Context processor for email subscription form static text
    '''
    return {
        'email_sub_text_1': 'Get Our\nLatest Offers & News',
        'email_sub_text_2': 'Subscribe for the news letter',
        'email_sub_text_1_var2': 'Get promotions & updates!',
        'email_sub_text_2_var2': 'Only what your loved ones would love.',
        'email_sub_form_placeholder': 'Your email here',
        'email_sub_button_text': 'Subscribe',
        }

def header_static_text(request):
    '''
    Context processor for header static text
    '''
    return  {
            'home': 'Home',
            'shop': 'Shop',
            'about': 'About Us',
            'contact': 'Contact',
            'account': 'Account',
            'search_placeholder': 'Search products',
        }

def footer_static_text(request):
    '''
    Context processor for footer static text
    '''
    return {
        'footer_text': {
            'company_slogan': 'Only what your loved ones would like.',
            'quick_links_title': 'Quick Links',
            'quick_links': {
                'about': 'About Us',
                'contact': 'Contact Us',
            },
            'support_title': 'Support',
            'support_links': {
                'faq': 'Frequently Asked Questions',
                'terms': 'Terms & Conditions',
            },
        }
    }

def about_static_text(request):
    '''
    Context processor for about page static text
    '''
    return {
        'about_text': {
            'page_title': 'About Us',
            'mission': {
                'title': 'Our Mission',
                'description': ('Placeholder text placeholder text placeholder text placeholder text '
                                'placeholder text placeholder text 69 placeholder text placeholder text '
                                'placeholder text placeholder text placeholder text placeholder text.'),
            },
            'feature': {
                'title': 'Placeholder text 69 placeholder text 69 placeholder text',
                'description': 'Placeholder text 69 placeholder text 69 placeholder text',
                'items': {
                    'credit_card': 'Credit Card Support',
                    'online_order': 'Online Order',
                    'free_delivery': 'Free Delivery',
                    'gift': 'Product with Gift',
                }
            },
        }
    }

def index_static_text(request):
    '''
    Context processor for index page static text
    '''
    return {
        'index_text': {
            'hero': {
                'discount': 'Up to 90% Discounts!',
                'title_1': 'Loved ones',
                'title_2': 'Collection',
                'subtitle': 'Best Cloth Collection By 2024!',
                'button': 'Shop Now',
            },
            'best_collection': {
                'left': {
                    'title': 'Placeholder text',
                    'description': 'Placeholder text.',
                    'button': 'Shop Now',
                },
                'right': {
                    'item1': {
                        'title': 'Placeholder\nText',
                    },
                    'item2': {
                        'title': 'Placeholder\nText',
                    },
                    'item3': {
                        'title': 'Placeholder\nText',
                    },
                },
            },
            'best_product': {
                'vertical_text': 'King',
                'title': 'Placeholder\nText',
                'description': 'Placeholder text.',
                'button': 'Shop Now',
            },
            'shop_method': {
                'shipping': {
                    'title': 'Free Shipping Method',
                    'description': 'Placeholder text 69',
                },
                'payment': {
                    'title': 'Secure Payment System',
                    'description': 'Placeholder text 69',
                },
                'refund': {
                    'title': '30 Full Refund',
                    'description': 'Placeholder text 69',
                },
            },
        }
    }

def contact_static_text(request):
    '''
    Context processor for contact page static text
    '''
    return {
        'contact_text': {
            'page_title': 'Contact Us',
            'section_title': 'Get in Touch',
            'form': {
                'message_placeholder': 'Enter Message',
                'name_placeholder': 'Enter your name',
                'email_placeholder': 'Email',
                'subject_placeholder': 'Enter Subject',
                'button_text': 'Send',
            },
            'info': {
                'email_subtitle': 'Send us your query anytime!',
                'no_contact_message': "We don't have no contact information. Gerara here man!",
            }
        }
    }

def product_list_static_text(request):
    '''
    Context processor for product list page static text
    '''
    return {
        'product_list_text': {
            'page_title': 'Product List',
            'filter': {
                'clear_button': 'Clear filter',
                'search_placeholder': 'Search by name',
                'category_default': 'Category',
                'animal_type_default': 'Animal Type',
            },
            'load_more': {
                'button_text': 'Load More',
            },
        }
    }

def single_product_static_text(request):
    '''
    Context processor for single product page static text
    '''
    return {
        'single_product_text': {
            'page_title': 'Product Details',
            'quantity': {
                'label': 'Quantity',
                'min': '1',
                'max': '20',
            },
            'cart': {
                'add_button': 'add to cart',
            },
        }
    }

def auth_static_text(request):
    '''
    Context processor for authentication-related pages static text
    '''
    return {
        'login_text': {
            'page_title': 'Login',
            'signup_section': {
                'title': 'New to our Shop?',
                'subtitle': ('There are advances being made in science and technology everyday, '
                             'and a good example of this is you.'),
                'button': 'Create an Account',
            },
            'signin_section': {
                'title': 'Welcome Back !',
                'subtitle': 'Please Sign in now',
                'email_placeholder': 'E-mail',
                'password_placeholder': 'Password',
                'button': 'log in',
            },
        },
        'registration_text': {
            'page_title': 'Registration',
            'form_section': {
                'title': 'Welcome!',
                'subtitle': 'Please fill the form to register',
                'email_placeholder': 'E-mail',
                'password_placeholder': 'Password',
                'confirm_password_placeholder': 'Repeat password',
                'button': 'register',
            },
        },
        'user_account_text': {
            'page_title': 'Your blank account',
            'content': {
                'title': 'Congratulations, you are logged in now!',
                'subtitle': 'Unfortunately, I had no HTML template for user member area, so this is just a text.',
                'what_next': 'What can you do?',
                'logout_button': 'LOGOUT',
            },
        },
        'logout_text': {
            'page_title': 'Logout page',
            'content': {
                'title': "Great, you've just logged out!",
                'subtitle': 'Unfortunately, I had no HTML template for user member area, so this is just a text.',
                'what_next': 'What can you do?',
                'login_button': 'LOGIN AGAIN',
            },
        },
    }

def checkout_flow_static_text(request):
    '''
    Context processor for cart-related pages static text
    '''
    return {
        'cart_text': {
            'page_title': 'Shopping Cart',
            'table': {
                'headers': {
                    'product': 'Product',
                    'price': 'Price',
                    'quantity': 'Quantity',
                    'total': 'Total',
                },
                'buttons': {
                    'update': 'Update',
                    'remove': 'Remove',
                    'clear': 'Clear Cart',
                },
            },
            'summary': {
                'subtotal': 'Subtotal',
            },
            'buttons': {
                'shop_more': 'Shop More',
                'checkout': 'Checkout',
            },
        },
        'checkout_text': {
            'page_title': 'Checkout',
            'order_summary': {
                'title': 'Your Order',
                'headers': {
                    'product': 'Product',
                    'total': 'Total',
                },
                'summary': {
                    'subtotal': 'Subtotal',
                    'shipping': 'Shipping',
                    'shipping_cost': 'Free',
                    'total': 'Total',
                },
            },
            'shipping_details': {
                'title': 'Shipping Details',
                'form': {
                    'first_name': {
                        'placeholder': 'First name *',
                    },
                    'last_name': {
                        'placeholder': 'Last name *',
                    },
                    'company': {
                        'placeholder': 'Company name',
                    },
                    'phone': {
                        'placeholder': 'Phone number *',
                    },
                    'email': {
                        'placeholder': 'Email *',
                    },
                    'country': {
                        'placeholder': 'Country *',
                    },
                    'address_1': {
                        'placeholder': 'Address *',
                    },
                    'address_2': {
                        'placeholder': 'Apt, suite, unit, floor, etc.',
                    },
                    'city': {
                        'placeholder': 'City/Town *',
                    },
                    'zip': {
                        'placeholder': 'Postcode/ZIP *',
                    },
                    'notes': {
                        'placeholder': 'Order Notes',
                    },
                },
                'button': 'Finalize',
            },
        },
        'confirmation_text': {
            'page_title': 'Confirmation',
            'message': {
                'title': 'Thank you! Your order has been received.',
                'subtitle': "We're on it and would contact you shortly",
            },
        },
    }
