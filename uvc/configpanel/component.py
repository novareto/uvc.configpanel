# -*- coding: utf-8 -*-

import grok
from uvc.configpanel import IConfigurablePlugin
from zope.cachedescriptors.property import CachedProperty
from zeam.form.base import Fields


class Plugin(grok.GlobalUtility):
    grok.baseclass()
    grok.provides(IConfigurablePlugin)

    title = u"Base plugin"
    description = u"Base configurable plugin."

     def __call__(self, *args, **kwargs):
         raise NotImplementedError('Please override.')

     def getInterfaces(self):
         raise NotImplementedError('Please override.')

     @CachedProperty
     def configuration_fields(self):
         ifaces = self.getInterfaces()
         return Fields(*ifaces)
