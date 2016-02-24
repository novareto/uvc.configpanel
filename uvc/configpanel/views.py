# -*- coding: utf-8 -*-

import grok
import uvcsite
from .traversal import Configurator
from .vocabulary import configurable_plugins


grok.templatedir('templates')


class ConfiguratorIndex(uvcsite.Page):
    grok.name('index.html')
    grok.context(Configurator)

    def update(self):
        self.plugins = configurable_plugins()
