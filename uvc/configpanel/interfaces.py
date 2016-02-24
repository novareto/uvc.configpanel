# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute
from zope.component.interfaces import IFactory


class IPluginConfiguration(Interface):
    pass


class IConfigurablePlugin(IFactory):
    pass
