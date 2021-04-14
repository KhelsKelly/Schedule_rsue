from django.db import models
from django.utils.translation import gettext_lazy as _


class Professor(models.Model):
    first_name = models.CharField(
        _('имя'),
        max_length=40,
        default='NN-препод.',
    )
    last_name = models.CharField(
        _('фамилия'),
        max_length=40,
        null=True,
    )
    patronym = models.CharField(
        _('отчество'),
        max_length=40,
        null=True,
    )
    position = models.ForeignKey(
        'api.Position',
        on_delete=models.SET_DEFAULT,
        related_name='professors',
        default=1,
    )

    class Meta:
        app_label = 'api'
