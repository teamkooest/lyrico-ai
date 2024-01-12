from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import NewUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password', 'is_staff', 'is_superuser', 'is_active', 'is_logged_in', 'is_verified', 'is_premium', 'is_deleted', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if 'username' in self.initial_data:
            existing_user = NewUser.objects.exclude(id=getattr(self.instance, 'id', None)).filter(username=value)
            if existing_user.exists():
                raise serializers.ValidationError('Username already exists.')
        return value
    

    def validate_email(self, value):
        if 'email' in self.initial_data:
            existing_user = NewUser.objects.exclude(id=getattr(self.instance, 'id', None)).filter(email=value)
            if existing_user.exists():
                raise serializers.ValidationError('Email already exists.')
        return value
    

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value
    

    def validate_password_length(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long')
        return value
    

    def validate(self, data):
        if 'first_name' not in data or not data['first_name']:
            raise serializers.ValidationError({'first_name': 'First name is required'})
        
        if 'username' not in data or not data['username']:
            raise serializers.ValidationError({'username': 'User name is required'})
        
        return data