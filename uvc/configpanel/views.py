# -*- coding: utf-8 -*-

import grok
import uvcsite.browser
from .traversal import Configurator
from .vocabulary import configurable_plugins


grok.templatedir('templates')


class ConfiguratorIndex(uvcsite.browser.Page):
    grok.name('index')
    grok.context(Configurator)

    def update(self):
        self.plugins = configurable_plugins()
