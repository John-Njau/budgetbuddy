# import serializers
from rest_framework import serializers

from .models import Expense, Category


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

    def create(self, validated_data):
        return Expense.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



