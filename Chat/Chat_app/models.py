from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')

    def __str__(self):
        return f"Message from {self.author} to {self.recipient}"