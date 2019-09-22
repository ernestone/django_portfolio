from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=60,
                             unique_for_date="pub_date")
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
