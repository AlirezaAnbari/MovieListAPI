from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination 


class WatchListPagination(PageNumberPagination): 
    page_size = 4
    # page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = '10'
    last_page_strings = ['last_page', 'last', 'end']
    
    
class WatchListLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    
    
class WatchListCursorPagination(CursorPagination):
    page_size = 4
    ordering = '-created'
    
    