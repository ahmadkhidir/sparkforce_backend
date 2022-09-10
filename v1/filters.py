from django_filters import rest_framework as filters

class LearningContentFilter(filters.FilterSet):
    cost = filters.NumberFilter(field_name="cost", lookup_expr='gte')
    type = filters.CharFilter(field_name="type", lookup_expr='eq')
    posted_gte = filters.DateFilter(field_name="time_posted", lookup_expr='gte')
    posted_lte = filters.DateFilter(field_name="time_posted", lookup_expr='lte')


class VolunteerOpportunityFilter(filters.FilterSet):
    point = filters.NumberFilter(field_name="point", lookup_expr='gte')
    type = filters.CharFilter(field_name="type", lookup_expr='eq')
    posted_gte = filters.DateFilter(field_name="time_posted", lookup_expr='gte')
    posted_lte = filters.DateFilter(field_name="time_posted", lookup_expr='lte')