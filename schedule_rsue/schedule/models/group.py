from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    name = models.CharField(
        _('название группы'),
        max_length=10,
    )
    year = models.IntegerField(
        _('курс'),
        validators=[MinValueValidator(1),
                    MaxValueValidator(5)]
    )
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

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'
