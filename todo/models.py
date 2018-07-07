from django.db import models
from django.urls import reverse

# Create your models here.


class ListElement(models.Model):
    text = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def get_absolute_url(self):
        return reverse('index', kwargs={'pk': self.})
