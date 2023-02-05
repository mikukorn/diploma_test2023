from django.core.paginator import Paginator
from django.conf import settings


def paginator(tests_list, request):
    paginator = Paginator(tests_list, settings.PAGE_LIMIT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj