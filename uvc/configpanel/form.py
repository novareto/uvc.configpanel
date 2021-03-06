# -*- coding: utf-8 -*-

import grok
import uvcsite.browser
from zeam.form.base import action, SUCCESS, FAILURE, Fields
from zeam.form.base.datamanager import DictDataManager
from zope.component import getUtility
from zope.cachedescriptors.property import CachedProperty
from .interfaces import IConfigurablePlugin, IPluginConfiguration


class Configure(uvcsite.browser.Form):
    grok.context(IPluginConfiguration)
    grok.name("index")
    grok.require("uvc.ManageCoUsers")

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
        return self.factory.configuration_fields

    @action(u"Speichern")
    def save_configuration(self):
        data, errors = self.extractData()
        if errors:
            self.flash("Es ist ein Fehler aufgetreten.")
            return FAILURE

        item = self.getContent()
        item.update(data)
        self.flash("Ihre Einstellungen wurden gespeichert.")
        return SUCCESS
