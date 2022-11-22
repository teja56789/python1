from django.shortcuts import render
from rest_framework import viewsets
from .models import Item,offer
from .serializers import ItemSerializer,offerSerializer
from rest_framework import permissions

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer
    permission_classes=[permissions.AllowAny]
    
class offerViewSet(viewsets.ModelViewSet):
    queryset=offer.objects.all()
    serializer_class=offerSerializer
    permission_classes=[permissions.AllowAny]