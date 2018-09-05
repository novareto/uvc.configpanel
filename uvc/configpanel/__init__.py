# -*- coding: utf-8 -*-

import logging
from .traversal import get_plugin_configuration, Configuration
from .interfaces import IConfigurablePlugin, IPluginConfiguration, IConfigurator
from .component import Plugin


logger = logging.getLogger('uvcsite.uvc.configpanel')


def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)
