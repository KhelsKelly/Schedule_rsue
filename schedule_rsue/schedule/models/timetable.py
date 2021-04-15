from django.db import models
from django.utils.translation import gettext_lazy as _


class Timetable(models.Model):
    time_from = models.TimeField(_('с:'))
    time_until = models.TimeField(_('до:'))

    def __str__(self):
        return f'{self.time_from}—{self.time_until}'

    class Meta:
        app_label = 'api'
