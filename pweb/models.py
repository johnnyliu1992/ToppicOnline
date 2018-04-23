from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='toppic_data_to_use/')
    uploaded_at = models.DateTimeField(auto_now_add=True)