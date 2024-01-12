from django.db import models
from apps.api.users.models import NewUser

"""
    The `Chat` class represents a chat message with a user, message content, and timestamps, and can be
    ordered by creation time.
"""
class Chat(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    message = models.TextField()
    is_user = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.is_user:
            return f'{self.user} - {self.message}'
        else:
            return f'Vocale AI - {self.message}'

    class Meta:
        ordering = ['-created_at']
