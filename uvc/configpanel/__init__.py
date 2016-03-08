import logging
from .traversal import get_config, Configuration
from .interfaces import IConfigurablePlugin, IPluginConfiguration, IConfigurator


logger = logging.getLogger('uvcsite.uvc.configpanel')

def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)


