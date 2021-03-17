from django.db import models

class ParsingResults(models.Model):
    date = models.DateField("Date", auto_now_add=True)
    slot_1 = models.CharField('Uptime', max_length=500, blank=True, null=True, default="")
    slot_2 = models.CharField('Fee',max_length=500, blank=True, null=True, default="")
    slot_3 = models.CharField('Teme left', max_length=500, blank=True, null=True, default="")
