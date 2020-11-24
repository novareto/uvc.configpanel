# -*- coding: utf-8 -*-

import grok
import uvcsite.browser
from .vocabulary import configurable_plugins
from .interfaces import IConfigurator


grok.templatedir('templates')


class ConfiguratorIndex(uvcsite.browser.Page):
    grok.name('index')
    grok.context(IConfigurator)

    def update(self):
        self.plugins = configurable_plugins()
