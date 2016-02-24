import logging
logger = logging.getLogger('uvcsite.uvc.configpanel')

def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)


import grok
from zope.interface import Interface
from zope.schema import Bool, TextLine
from .interfaces import IConfigurablePlugin
from .traversal import Configuration
from zope.interface import directlyProvides


class IMyConf(Interface):
    choice = Bool(
        title=u'Are you a man ?',
        required=True)

    fullname = TextLine(
        title=u'Enter your full name',
        required=True)


class MyPlugin(grok.GlobalUtility):
    grok.name('mytestplugin')
    grok.provides(IConfigurablePlugin)
    
    title = u"My Plugin"
    description = u"Some description"
    
    def __call__(self, *args, **kwargs):
        conf = Configuration(**kwargs)
        directlyProvides(conf, IMyConf)
        return conf

    def getInterfaces(self):
        return [IMyConf]
