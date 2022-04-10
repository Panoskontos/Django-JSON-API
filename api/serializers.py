# Careful
from rest_framework_json_api import serializers
from .models import *


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
