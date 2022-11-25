from django.db import models

# Create your models here.


class task(models.Model):
    describtion=models.CharField(max_length=45)
    done=models.BooleanField(default=False)

    def __str__(self):
        return self.describtion