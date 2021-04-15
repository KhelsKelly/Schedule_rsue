from django.db import models
from django.utils.translation import gettext_lazy as _


class Faculty(models.Model):
    name = models.CharField(
        _('название факультета'),
        max_length=80,
    )
    abbreviation = models.CharField(
        _('аббревиатура'),
        max_length=20,
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'
