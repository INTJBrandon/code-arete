from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class POST(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    Photo = models.ImageField(upload_to='images/', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['-date_posted']
    
    
    def __str__(self):
        return self.title
