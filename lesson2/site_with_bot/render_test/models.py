from django.db import models

# Create your models here.


class SampleModel(models.Model):

    username = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        managed = True
        verbose_name = 'SampleModel'
        verbose_name_plural = 'SampleModel'