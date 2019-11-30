from rest_framework.serializers import ModelSerializer
from .models import Item


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ItemSerializer, self).to_representation(instance)
        representation['category_name'] = instance.category.title
        return representation
