from django.db import models
from django.utils.translation import gettext_lazy as _

from django_fsm_enhanced import BaseStateLog, EnhancedFSMField


class BlogAuthorStates(models.TextChoices):
    ACTIVE = "ACTIVE", _("Active")
    INACTIVE = "INACTIVE", _("Inactive")
    ARCHIVED = "ARCHIVED", _("Archived")


class BlogAuthorStateLog(BaseStateLog):
    pass


class BlogAuthor(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    state = EnhancedFSMField(
        default=BlogAuthorStates.ACTIVE,
        choices=BlogAuthorStates.choices,
        log=BlogAuthorStateLog,
    )


class BlogPostStates(models.TextChoices):
    DRAFT = "DRAFT", _("Draft")
    PUBLIC = "PUBLIC", _("Public")
    PRIVATE = "PRIVATE", _("Private")
    ARCHIVED = "ARCHIVED", _("Archived")


class BlogPostStateLog(BaseStateLog):
    pass


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField(blank=True, default="")

    authors = models.ManyToManyField(BlogAuthor, related_name="posts")

    state = EnhancedFSMField(
        default=BlogPostStates.DRAFT,
        choices=BlogPostStates.choices,
        log=BlogPostStateLog,
    )
