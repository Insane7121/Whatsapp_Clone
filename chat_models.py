# chat/models.py
from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    sender = models.ForeignKey(Contact, related_name="sent_messages", on_delete=models.CASCADE)
    recipient = models.ForeignKey(Contact, related_name="received_messages", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient}"

class Chat(models.Model):
    participants = models.ManyToManyField(Contact)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return f"Chat between {', '.join([str(p) for p in self.participants.all()])}"
