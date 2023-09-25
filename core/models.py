from django.db import models
from django.utils.translation import gettext as _


class Item(models.Model):
    value = models.CharField(verbose_name=_("Value"), max_length=255)
    turn = models.BigIntegerField(verbose_name=_("Turn"), null=True, blank=True)
    passed = models.BooleanField(verbose_name=_("Passed"), default=False, blank=True)

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
