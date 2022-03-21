from datetime import datetime

from django.db import models

from abstracts.models import AbstractDateTime
import uuid

from django.contrib.auth.models import User


class Task(AbstractDateTime):

    lead_time = models.DateTimeField(
        null=False,
        blank=True,
        auto_now_add=True,
    )

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
    )

    title = models.CharField(
        max_length=100,
    )

    is_active = models.BooleanField(
        'Активность', 
        default=True,
    )

    def __str__(self) -> str:
        return f'Задание: {self.title}'


    class Meta:
        ordering = (
            'datetime_created',
        )

        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'