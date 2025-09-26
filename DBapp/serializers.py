from rest_framework import serializers
from .models import Flat,Owner


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flat
        fields='__all__'

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Owner
        fields='__all__'