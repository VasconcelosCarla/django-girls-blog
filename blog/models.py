from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    
    def __str__ (self):
        return self.title
