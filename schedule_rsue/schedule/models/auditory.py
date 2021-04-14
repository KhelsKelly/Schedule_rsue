from django.db import models
from django.utils.translation import gettext_lazy as _


class Auditory(models.Model):
    audit_num = models.CharField(
        _('номер аудитории'),
        max_length=10,
    )
    building = models.ForeignKey(
        'api.Building',
        on_delete=models.CASCADE,
        related_name='auditories',
    )

    class Meta:
        app_label = 'api'
