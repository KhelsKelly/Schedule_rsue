from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

User = settings.AUTH_USER_MODEL


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('электронная почта'),
        unique=True,
    )
    is_staff = models.BooleanField(
        _('статус персонала'),
        default=False,
    )
    is_active = models.BooleanField(
        _('активен'),
        default=True,
    )
    date_joined = models.DateTimeField(
        _('дата присоединения'),
        auto_now_add=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('пользователь')
        verbose_name_plural = _('пользователи')
