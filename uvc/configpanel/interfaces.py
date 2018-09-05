# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute
from zope.component.interfaces import IFactory


class IConfigurator(Interface):
    pass


class IPluginConfiguration(Interface):
    pass


class IConfigurablePlugin(IFactory):

    configuration_fields = Attribute(
        u"List of fields used to configure the plugin")
