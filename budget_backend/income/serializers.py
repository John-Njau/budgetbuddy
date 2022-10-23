from rest_framework import serializers
from .models import Income, Source

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('id','amount','notes','source_name','start_date','end_date')

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id','name')
# 
# 
# # Path: budget_backend\income\views.py
# # Compare this snippet from budget_backend\budget\views.py:
