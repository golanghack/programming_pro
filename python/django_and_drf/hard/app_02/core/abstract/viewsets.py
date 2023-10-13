from rest_framework import viewsets
from rest_framework import filters

class AbstractViewSet(viewsets.ModelViewSet):
    """Abstract View set"""

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated', 'created']
    ordering = ['-updated']
    