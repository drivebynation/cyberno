from django.db import models
from django.utils.translation import gettext as _
from .exceptions import ExistError, ArrivedTurn, EmptyQueueError


class Item(models.Model):
    container = []
    value = models.CharField(verbose_name=_("Value"), max_length=255, unique=True)
    passed = models.BooleanField(verbose_name=_("Passed"), default=False, blank=True)

    @classmethod
    def add(cls, value):
        if cls.objects.filter(value=value).exists():
            raise ExistError("The desired item already is in the queue!")
        cls.container.insert(0, value)
        cls.objects.create(value=value, turn=len(cls.container))

    @classmethod
    def remove(cls):
        if len(cls.container) == 0:
            raise EmptyQueueError("Queue is Empty!")
        item = cls.container.pop()
        data = cls.objects.get(value=item)
        data.passed = True
        return item

    @classmethod
    def get_turn(cls, value):
        item = cls.objects.filter(value=value)
        if item.passed:
            raise ArrivedTurn("This Item's turn has already arrived!")
        turn = len(cls.container) - cls.container.index(value)
        return f"{value} is in turn {turn}"

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
