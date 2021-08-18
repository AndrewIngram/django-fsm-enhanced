import sys

from django.db import connection, models
from django.db.backends import utils
from django.db.models.fields.related import lazy_related_operation
from django.utils.translation import gettext_lazy as _

from django_fsm import FSMField, FSMFieldDescriptor

from .models import BaseStateLog


# def create_state_log_model(field, klass):
#     source_model_name = klass._meta.model_name
#     name = "%s%sLog" % (klass._meta.object_name, field.name.title())

#     meta = type(
#         "Meta",
#         (),
#         {
#             "db_table": field._get_log_db_table(klass._meta),
#             "auto_created": klass,
#             "app_label": klass._meta.app_label,
#             "db_tablespace": klass._meta.db_tablespace,
#             "managed": True,
#             "verbose_name": _("%(model)s state log") % {"model": source_model_name},
#             "verbose_name_plural": _("%(model)s state logs")
#             % {"model": source_model_name},
#             "apps": field.model._meta.apps,
#         },
#     )

#     return type(
#         name,
#         (BaseStateLog,),
#         {
#             "Meta": meta,
#             "__module__": klass.__module__,
#             "obj": models.ForeignKey(
#                 klass,
#                 related_name="%s_logs" % name,
#                 db_tablespace=field.db_tablespace,
#                 on_delete=models.CASCADE,
#             ),
#         },
#     )


class EnhancedFSMFieldDescriptor(FSMFieldDescriptor):
    pass


class EnhancedFSMField(FSMField):
    descriptor_class = EnhancedFSMFieldDescriptor

    def __init__(self, *args, **kwargs):
        self.log_cls = kwargs.pop("log", None)
        super().__init__(*args, **kwargs)

    def _get_log_db_table(self, opts):
        from django.db.backends import utils

        log_table_name = "%s_%s_log" % (utils.strip_quotes(opts.db_table), self.name)
        return utils.truncate_name(log_table_name, connection.ops.max_name_length())

    def contribute_to_class(self, cls, name, **kwargs):
        super().contribute_to_class(cls, name, **kwargs)

        if not cls._meta.abstract and self.log_cls:
            self.log_cls.add_to_class(
                "obj",
                models.ForeignKey(
                    cls,
                    related_name="%s_logs" % name,
                    on_delete=models.CASCADE,
                ),
            )
