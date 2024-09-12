from dbapp.models import Employee
from rest_framework import serializers
class empserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"