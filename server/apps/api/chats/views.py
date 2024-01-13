from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Chat
from .serializers import ChatSerializer

def generate_lyrics(prompt):
    lyrics = f'Your name is Vocale, and act as a song writer with 10 years of experience in the music industry. You have written a song for a famous singer, and you are now ready to release it. So generate me title and lyrics based on this: {prompt}. Make sure to include verses, chorus, and bridge. The song should be at least minutes long.'
    return lyrics

class ChatListView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True, context={'request': request})
        if instance:
            return Response({
                'chats': serializer.data,
                'status': 'success',
                'message': 'Chats retrieved successfully.',
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'chats': [],
                'status': 'success',
                'message': 'No chats found.',
            }, status=status.HTTP_200_OK)
        
    

