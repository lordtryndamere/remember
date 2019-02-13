from django.db import models

# Create your models here.
class Entry(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def  __str__(self):
        return " Entry #{} ".format (self.id)

    class Meta:
        verbose_name_plural = 'entries'