from django.db import models
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    group_name = models.CharField(
        _('название группы'),
        max_length=10,
    )
    year = models.IntegerField(_('курс'))
    faculty = models.ForeignKey(
        'api.Faculty',
        on_delete=models.CASCADE,
        related_name='groups',
    )
    cafedra = models.ForeignKey(
        'api.Cafedra',
        on_delete=models.CASCADE,
        related_name='groups',
    )

    class Meta:
        app_label = 'api'
