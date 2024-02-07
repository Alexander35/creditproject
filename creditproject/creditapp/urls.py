from django.urls import path
from .views import get_vendors

urlpatterns = [
    path('vendors/<contract_id>/', get_vendors, name='get_vendors'),
]
