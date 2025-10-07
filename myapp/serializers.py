from rest_framework.serializers import ModelSerializer
from .models import Product, Category, Cart

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['products'] = ProductSerializer(instance.product_set.all(), many=True).data
        return representation

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['products'] = ProductSerializer(instance.products).data
        return representation
    