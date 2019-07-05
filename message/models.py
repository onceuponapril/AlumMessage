from django.db import models
from django.urls import reverse

# Create your models here.
class Message(models.Model):
    msg_id = models.AutoField(primary_key = True)
    sender = models.TextField(null = False, max_length=20)
    receiver = models.TextField(null = False, max_length=20)
    content = models.TextField(null = False, max_length=500)
    timeStamp =  models.DateTimeField(auto_now_add=True)

    class Meta:
            managed = True
            db_table = 'message'

    def __str__(self):
        return self.content[:50]
    
    def get_absolute_url(self):
        return reverse('send')    


class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    uniqname = models.TextField(null = False, max_length = 100, unique = True)
    
    class Meta:
        managed = True
        db_table = 'user'

    def __str__(self):
        return self.uniqname