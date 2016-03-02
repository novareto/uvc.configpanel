# -*- coding: utf-8 -*-

import grok
import uvcsite
from zope.component import getUtility
from zope.traversing.interfaces import ITraversable
from zope.location import Location, LocationProxy
from BTrees.OOBTree import OOBTree
from persistent.dict import PersistentDict
from .interfaces import IConfigurablePlugin, IPluginConfiguration
from zope.interface import alsoProvides, Interface


def get_config(name):
    homefolder = uvcsite.getHomeFolder(uvcsite.getRequest())
    config = homefolder.get('__config__', None)
    if config:
        return config.get(name)
    return 


class Configurator(OOBTree):
    pass


class Configuration(PersistentDict, Location):
    grok.implements(IPluginConfiguration)


class PluginConfigurationNamespace(grok.MultiAdapter):
    grok.name('plugins')
    grok.provides(ITraversable)
    grok.adapts(Interface, Interface)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def traverse(self, name, ignore):
        homefolder = uvcsite.getHomeFolder(self.request)
        if '__config__' not in homefolder:
            homefolder['__config__'] = Configurator()
        configurator = homefolder['__config__']
        if not name:
            return configurator
        elif name not in configurator:
            config_item = getUtility(IConfigurablePlugin, name=name)
            configurator[name] = config_item()
        return LocationProxy(configurator[name], configurator, name)
