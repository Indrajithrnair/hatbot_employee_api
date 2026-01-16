from rest_framework import serializers
from .models import Employee
from rest_framework.exceptions import ValidationError

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee

        fields = [
            'id',
            'name',
            'email',
            'department',
            'role',
            'date_joined'
        ]

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    
    def validate_email(self, value):
        
        qs = Employee.objects.filter(email=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError("Email already exists..!")
        return value