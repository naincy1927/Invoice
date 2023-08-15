from rest_framework import viewsets
from .models import InvoiceDetail
from .serializers import InvoiceDetailSerializer



class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer