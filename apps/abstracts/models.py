from django.db import models
import uuid

class AbstractDateTime(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4, 
        editable=False)

    datetime_created = models.DateTimeField(
        verbose_name='Время создания',
        auto_now=True,
    )
    datetime_updated = models.DateTimeField(
        verbose_name='Время обновления',
        auto_now=True
    )
    datetime_deleted = models.DateTimeField(
        verbose_name='Время обновления',
        null=True,
        blank=True
    )

    class Meta():
        abstract = True
    
    def __str__(self) -> str:
        return f'Время создания - {self.datetime_created}  \
        Дата изменения - {self.datetime_updated}   \
        Дата удаления - {self.datetime_deleted}'

