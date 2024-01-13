from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            'user', 'message', 'is_user', 'created_at', 'updated_at'
        ]
    
    def validate(self, data):

        if 'prompt' not in data or not data['prompt']:
            raise serializers.ValidationError({'prompt': 'Prompt is required'})

        if 'message' not in data or not data['message']:
            raise serializers.ValidationError({'message': 'Message is required'})
        
        if 'is_user' not in data or not data['is_user']:
            raise serializers.ValidationError({'is_user': 'Is User is required'})
        
        return data