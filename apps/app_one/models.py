from django.db import models
from datetime import datetime, date

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# this is the database where messages will be stored
# many messages, one user
class Message(models.Model):
    user_id = models.ForeignKey(User, related_name="messages")
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# this is the database where comments on the messages will be stored
# many comments, many messages
# many comments, one user
class Comment(models.Model):
    message_id = models.ForeignKey(Message, related_name="comments", null=True)
    user_id = models.ForeignKey(User, related_name="comments")
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
