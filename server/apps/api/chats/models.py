from django.db import models
from apps.api.users.models import NewUser

class Chat(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    prompt = models.TextField(blank=True, null=True)
    message = models.TextField()
    is_user = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.is_user:
            return f'{self.user} - User Prompt: {self.prompt}'
        else:
            return f'Vocale AI - Generated Lyrics: {self.message}'

    class Meta:
        ordering = ['-created_at']
