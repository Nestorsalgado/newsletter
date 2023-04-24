
from django.db import models

class Email(models.Model):
    email=models.EmailField()
    titulo=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='email'
        verbose_name_plural='emails'

    def __str__(self):
        return self.email