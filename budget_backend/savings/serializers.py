from rest_framework import serializers

from .models import Saving

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'

    def create(self, validated_data):
        return Saving.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.target = validated_data.get('target', instance.target)
        instance.save()
        return instance

