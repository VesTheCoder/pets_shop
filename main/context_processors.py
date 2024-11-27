from .models import ShopContact

def search_query(request):
    '''
    Retrieves the search query from the request's GET parameters.

    Args:
        request: The HTTP request object.

    Returns:
        A dictionary containing the search query or an empty string if not present.
    '''
    return {'search_request': request.GET.get('search', '')}

def shop_contact(request):
    '''
    Retrieves the first ShopContact object from the database.
    Note: only one (first and only) shop contact is designed to exist.
    Args:
        request: The HTTP request object (unused in this function but required for context processors).

    Returns:
        A dictionary containing the first ShopContact object or None if not found.
    '''
    contact_info = ShopContact.objects.first()
    return {'shop_contact': contact_info}