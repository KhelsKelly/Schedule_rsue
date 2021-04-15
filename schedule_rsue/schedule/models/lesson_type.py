from django.db import models
from django.utils.translation import gettext_lazy as _


class LessonType(models.Model):
    name = models.CharField(
        _('вид занятия'),
        max_length=40,
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'
