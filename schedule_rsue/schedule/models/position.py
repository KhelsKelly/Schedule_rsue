from django.db import models
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    pos_name = models.CharField(
        _('должность'),
        max_length=80,
    )

    class Meta:
        app_label = 'api'
