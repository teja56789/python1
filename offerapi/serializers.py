from rest_framework import serializers
from .models import offer,Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        # fields = ['name','description','price','active','thumbnail']
        fields = '__all__'
        
        
class offerSerializer(serializers.ModelSerializer):
    class Meta:
        model= offer
        # fields = ['code','item','discount']
        fields = '__all__'