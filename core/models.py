from django.db import models
import uuid

class WeatherRecords(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField('city',max_length=100)
    temperature = models.IntegerField('temperature')
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.city}{self.temperature}{self.date}'

