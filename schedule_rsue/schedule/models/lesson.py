from django.db import models
from django.utils.translation import gettext_lazy as _


class Lesson(models.Model):
    name = models.ForeignKey(
        'api.LessonName',
        on_delete=models.CASCADE,
        related_name='lessons',
    )
    group = models.ForeignKey(
        'api.Group',
        on_delete=models.CASCADE,
        related_name='lessons',
    )
    auditory = models.ForeignKey(
        'api.Auditory',
        on_delete=models.CASCADE,
        related_name='lessons',
    )
    professor = models.ForeignKey(
        'api.Professor',
        on_delete=models.CASCADE,
        related_name='lessons',
    )
    timetable = models.ForeignKey(
        'api.Timetable',
        on_delete=models.CASCADE,
    )
    lesson_type = models.ForeignKey(
        'api.LessonType',
        on_delete=models.CASCADE,
        related_name='lessons',
        default=1,
    )
    even_week = models.BooleanField(
        _('чётная/нечётная неделя'),
        null=False,
    )
    DAYS = (
        (1, _('Понедельник')),
        (2, _('Вторник')),
        (3, _('Среда')),
        (4, _('Четверг')),
        (5, _('Пятница')),
        (6, _('Суббота')),
        (7, _('Воскресенье')),
    )
    day = models.IntegerField(
        _('день недели'),
        choices=DAYS,
    )

    def __str__(self):
        return f'{self.name}, {self.day}'

    class Meta:
        app_label = 'api'
        ordering = ['day', 'timetable']
