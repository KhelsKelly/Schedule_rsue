from django.db import models
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    name = models.CharField(
        _('должность'),
        max_length=80,
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'
