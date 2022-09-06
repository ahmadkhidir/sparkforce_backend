from rest_framework.pagination import LimitOffsetPagination

class LimitOffsetPaginationWeb(LimitOffsetPagination):
    default_limit = 20