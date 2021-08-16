from django.conf import settings
from django.db import models


class BaseStateLog(models.Model):
    source_state = models.CharField(
        "Source state",
        max_length=255,
        db_index=True,
        null=True,
        blank=True,
        default=None,
    )
    state = models.CharField("Target state", max_length=255, db_index=True)
    transition = models.CharField("Transition name", max_length=255, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    meta_data = models.JSONField(default=dict)  # type: ignore

    class Meta:
        abstract = True
