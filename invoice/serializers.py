from rest_framework import serializers
from .models import Invoice
from invoiceDetail.serializers import InvoiceDetailSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, required=False)

    class Meta:
        model = Invoice
        fields = '__all__'