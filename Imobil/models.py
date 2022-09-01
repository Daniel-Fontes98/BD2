from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    Gold_Access = models.BooleanField(default=False)
    image = models.ImageField(default='defaultHouse.jpg', upload_to='house_pics')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('imobil-detail', kwargs={'pk': self.pk})