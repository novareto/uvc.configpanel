# -*- coding: utf-8 -*-

import grok
from zope.interface import implementer, alsoProvides
from uvc.configpanel import IConfigurablePlugin, Configuration
from zope.cachedescriptors.property import CachedProperty
from zeam.form.base import Fields


@implementer(IConfigurablePlugin)
class Plugin(grok.GlobalUtility):
    grok.baseclass()
 
    title = u"Base plugin"
    description = u"Base configurable plugin."
    icon = "fas fa-plug"

    def __call__(self, *args, **kwargs):
        conf = Configuration(**kwargs)
        ifaces = self.getInterfaces()
        if ifaces:
            alsoProvides(conf, *ifaces)
        return conf

    def getInterfaces(self):
        return []

    @CachedProperty
    def configuration_fields(self):
        ifaces = self.getInterfaces()
        return Fields(*ifaces)
