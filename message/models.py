from django.db import models
from django.urls import reverse
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.
class Message(models.Model):
    msg_id = models.AutoField(primary_key = True)
    sender = models.CharField(null = False, max_length=20)
    receiver = models.CharField(null = False, max_length=20)
    content = models.TextField(null = False, max_length=500)
    timeStamp =  models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'message'

    def __str__(self):
        return self.content
        
    def get_absolute_url(self):
        return reverse('send')
