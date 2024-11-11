def search_query(request):
    return {
        'search_request': request.GET.get('search', '')
    }