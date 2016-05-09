# -*- coding: utf-8 -*-

import grok
import uvcsite
import datetime

from BTrees.OOBTree import OOBTree
from zope.interface import Interface
from zope.component import getUtility
from persistent.dict import PersistentDict
from zope.location import Location, LocationProxy
from zope.traversing.interfaces import ITraversable
from zope.dublincore.interfaces import IDCDescriptiveProperties
from .interfaces import IConfigurator, IConfigurablePlugin, IPluginConfiguration


class Configurator(OOBTree):
    grok.implements(IConfigurator, IDCDescriptiveProperties)

    title = u"Konfiguration"


class Configuration(PersistentDict, Location):
    grok.implements(IPluginConfiguration)


def get_config(name):
    homefolder = uvcsite.getHomeFolder(uvcsite.getRequest())
    config = homefolder.get('__config__', None)
    if config:
        return config.get(name)
    return


def get_plugin_configuration(homefolder=None, request=None, name=None):
    if homefolder is None:
        if request is None:
            request = uvcsite.getRequest()
        homefolder = uvcsite.getHomeFolder(request)
    if '__config__' not in homefolder:
        homefolder['__config__'] = Configurator()
    configurator = homefolder['__config__']
    if not name:
        return configurator
    elif name not in configurator:
        config_item = getUtility(IConfigurablePlugin, name=name)
        configurator[name] = config_item()
    return LocationProxy(configurator[name], configurator, name)


class PluginConfigurationNamespace(grok.MultiAdapter):
    grok.name('plugins')
    grok.provides(ITraversable)
    grok.adapts(Interface, Interface)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def traverse(self, name, ignore):
        return get_plugin_configuration(request=self.request, name=name)
