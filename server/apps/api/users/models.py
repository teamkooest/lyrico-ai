import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager

"""
	The `CustomAccountManager` class is a subclass of `BaseUserManager` that provides methods for
	creating superusers and regular users with specified fields.
"""
class CustomAccountManager(BaseUserManager):
    """
      	The function creates a superuser with the given email, username, first name, password, and other
      	optional fields.
      
		@param email: The email parameter is the email address of the user
		@param user_name: The username of the superuser
		@param first_name: The first name of the user
		@param password: The password parameter is used to specify the password for the superuser
		account
		@return: the result of calling the `create_user` method with the provided arguments and any
		additional keyword arguments passed in `other_fields`.
    """
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
      
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        
        return self.create_user(email, user_name, first_name, password, **other_fields)
    
    """
		The function creates a user with the provided email, username, first name, password, and any
		additional fields.
		
		@param email: The email parameter is the email address of the user being created
		@param user_name: The `user_name` parameter is used to specify the username for the user being
		created
		@param first_name: The first name of the user
		@param password: The password parameter is the password that the user wants to set for their
		account
		@return: the created user object.
    """
    def create_user(self, email, user_name, first_name, password, **other_fields):
      
        if not email:
            raise ValueError('You must provide an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        
        return user

"""
	The `NewUser` class is a model that represents a user with various fields such as email, username, first name, last name, roles, status, and timestamps.
"""
class NewUser(AbstractUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('email address', unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=True)

    # Roles
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Status
    is_active = models.BooleanField(default=False)
    is_logged_in = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']
    
    def __str__(self):
        return self.user_name + ", " + self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'