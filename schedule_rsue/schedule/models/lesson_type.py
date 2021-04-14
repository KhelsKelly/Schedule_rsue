from django.db import models
from django.utils.translation import gettext_lazy as _


class LessonType(models.Model):
    type_name = models.CharField(
        _('вид занятия'),
        max_length=40,
    )

    class Meta:
        app_label = 'api'
