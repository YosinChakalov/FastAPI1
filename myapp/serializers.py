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
        represent = super().to_representation(instance)
        represent['products'] = ProductSerializer(instance.product_set.all(), many=True).data
        return represent

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        
    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['products'] = ProductSerializer(instance.products).data
        return represent
    