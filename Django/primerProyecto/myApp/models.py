from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length="100")
    content = models.TextField()
    public = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)