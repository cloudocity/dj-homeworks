from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание',null=True)

class Measurement(models.Model):
    Sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='Sensor', verbose_name='ID')
    temperature = models.CharField(max_length=30, verbose_name='Температура')
    created_at = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
