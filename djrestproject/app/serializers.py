from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=['id','name','age','email','contact_no']
