# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from model_utils.managers import PassThroughManager
from model_utils.models import TimeStampedModel


class DeviceQuerySet(QuerySet):
    def for_user(self, user):
        return self.filter(user=user)


class Device(TimeStampedModel):
    user = models.ForeignKey(User, verbose_name=_(u"Device owner"), related_name='devices')
    device_id = models.CharField(max_length=50, verbose_name=_(u"Device ID"))
    name = models.CharField(max_length=100, verbose_name=_(u"Device name"))

    objects = PassThroughManager.for_queryset_class(DeviceQuerySet)()

    class Meta:
        verbose_name = _(u"Device")
        verbose_name_plural = _(u"Devices")
        ordering = ['-created']

    def __unicode__(self):
        return self.name