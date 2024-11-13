from .models import ShopContact

def search_query(request):
    return {'search_request': request.GET.get('search', '')}

def shop_contact(request):
    contact_info = ShopContact.objects.first()
    return {'shop_contact': contact_info}