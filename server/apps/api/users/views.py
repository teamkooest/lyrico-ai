from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from .models import NewUser
from .serializers import UserSerializer

class UserListView(ListAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True, context={'request': request})
        if instance:
            return Response({
                'users': serializer.data,
                'status': 'success',
                'message': 'Users retrieved successfully.',
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'users': [],
                'status': 'success',
                'message': 'No users found.',
            }, status=status.HTTP_200_OK)
        

class UserDetailView(RetrieveAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request': request})

        if instance:
            return Response({
                'user': serializer.data,
                'status': 'success',
                'message': 'User retrieved successfully.',
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'user': {},
                'status': 'success',
                'message': 'No user found.',
            }, status=status.HTTP_200_OK)


class UserRegistrationView(CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try: 
            serializer = self.get_serializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                'user': serializer.data,
                'status': 'success',
                'message': 'User created successfully.',
            }, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            errors = dict(e.detail)
            return Response({
                'user': {},
                'status': 'error',
                'message': 'User registration failed. Please check the errors.',
                'errors': errors,
            }, status=status.HTTP_400_BAD_REQUEST)
    

class UserUpdateView(UpdateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial, context={'request': request})
        
        try: 
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                'user': serializer.data,
                'status': 'success',
                'message': 'User updated successfully.',
            }, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            errors = dict(e.detail)
            return Response({
                'user': {},
                'status': 'error',
                'message': 'User update failed. Please check the errors.',
                'errors': errors,
            }, status=status.HTTP_400_BAD_REQUEST)

class UserHardDeleteView(DestroyAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        try:
            instance.delete()
            return Response({
                'user': {},
                'status': 'success',
                'message': 'User deleted successfully.',
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'user': {},
                'status': 'error',
                'message': 'User deletion failed. Please try again.',
            }, status=status.HTTP_400_BAD_REQUEST)
        
class UserSoftDeleteView(DestroyAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        try:
            instance.soft_delete()
            return Response({
                'user': {},
                'status': 'success',
                'message': 'User deleted successfully.',
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'user': {},
                'status': 'error',
                'message': 'User deletion failed. Please try again.',
            }, status=status.HTTP_400_BAD_REQUEST)