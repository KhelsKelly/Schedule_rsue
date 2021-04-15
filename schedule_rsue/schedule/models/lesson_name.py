from django.db import models
from django.utils.translation import gettext_lazy as _


class LessonName(models.Model):
    name = models.CharField(
        _('название пары'),
        max_length=60,
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'
