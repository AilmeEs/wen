from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=20)
    intro=models.TextField()
    publish=models.DateTimeField(default=timezone.now())
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title