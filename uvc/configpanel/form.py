# -*- coding: utf-8 -*-

import grok
import uvcsite
from zeam.form.base import action, SUCCESS, FAILURE
from zeam.form.base.datamanager import DictDataManager
from zope.component import getUtility
from zope.cachedescriptors.property import CachedProperty
from .interfaces import IConfigurablePlugin, IPluginConfiguration


class Configure(uvcsite.Form):
    grok.context(IPluginConfiguration)
    grok.name('index.html')
    #uvcsite.require()

    ignoreContent = False
    ignoreRequest = False
    dataManager = DictDataManager

    @CachedProperty
    def factory(self):
        return getUtility(IConfigurablePlugin, name=self.context.__name__)

    @CachedProperty
    def label(self):
        return self.factory.title
    
    @CachedProperty
    def fields(self):
        return uvcsite.Fields(*self.factory.getInterfaces())

    @action(u"Save")
    def save_configuration(self):
        data, errors = self.extractData()
        if errors:
            self.flash('An error happened')
            return FAILURE

        item = self.getContent()
        item.update(data)
        self.flash('Configuration successful')
        return SUCCESS
