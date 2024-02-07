from django.http import JsonResponse
from .models import Contract, Product


def get_vendors(request, contract_id):
    credit_order_id = Contract.objects.filter(id=contract_id).values_list('credit_order_id', flat=True).first()

    vendor_ids = Product.objects.filter(credit_order_id=credit_order_id).values_list('vendor_id', flat=True).distinct()

    data = {'message': [v_id for v_id in vendor_ids]}
    return JsonResponse(data)
