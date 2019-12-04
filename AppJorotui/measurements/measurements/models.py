from django.db import models

class Measurement(models.Model):
    usuario = models.IntegerField(null=False, default=None)
    value = models.FloatField(null=True, blank=True, default=None)
    unit = models.IntegerField(null=False, default=None)
    correo = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)