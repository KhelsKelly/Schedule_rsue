from django.db import models
from django.utils.translation import gettext_lazy as _


class Cafedra(models.Model):
    name = models.CharField(
        _('название кафедры'),
        max_length=80,
    )
    faculty = models.ForeignKey(
        'api.Faculty',
        on_delete=models.CASCADE,
        related_name='cafedras',
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'
