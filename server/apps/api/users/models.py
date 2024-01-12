import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_verified', True)
        other_fields.setdefault('is_premium', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        
        return self.create_user(email, username, first_name, password, **other_fields)
    
    def create_user(self, email, username, first_name, password, **other_fields):
      
        if not email:
            raise ValueError('You must provide an email address.')
        
        if not username:
            raise ValueError('You must provide a username.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        
        return user

class NewUser(AbstractUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('email address', unique=True)
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

    def soft_delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save(using=using, update_fields=['is_deleted'])
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']
    
    def __str__(self):
        return f'{self.username} ({self.email})'

    class Meta:
        verbose_name = 'All'
        verbose_name_plural = 'All'