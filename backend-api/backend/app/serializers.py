from rest_framework import serializers
from app.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students 
        fields=(
            'studentid',
            'fname',
            'lname',
            'address',
            'email'
        )
