from django.db import models

# Create your models here.


class booking(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    number_of_people = models.IntegerField(null=False, blank=False)
    time_and_date = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.name
