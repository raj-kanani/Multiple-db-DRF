from django.db import models


class Administrator(models.Model):
    # objects = None
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    # class Meta:
    #     app_label = 'Administrator'

    def __str__(self):
        return self.username
