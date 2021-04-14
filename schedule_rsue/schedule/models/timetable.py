from django.db import models
from django.utils.translation import gettext_lazy as _


class Timetable(models.Model):
    time_from = models.TimeField(_('с:'))
    time_until = models.TimeField(_('до:'))

    class Meta:
        app_label = 'api'
