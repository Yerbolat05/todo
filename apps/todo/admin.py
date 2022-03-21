from django.contrib import admin

from .models import (
    Task,
)

class TaskAdmin(admin.ModelAdmin):

    readoly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )

admin.site.register(
    Task, TaskAdmin,
)