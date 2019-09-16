# -*- coding: utf-8 -*-

import grok
import uvcsite.browser.layout.menu
import uvcsite.browser.layout.slots.interfaces
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface


class MyPrefsMenu(uvcsite.browser.layout.menu.MenuItem):
    grok.name('my_prefs_menu')
    grok.title(u'Erweiterte Einstellungen')
    grok.require('uvc.ManageCoUsers')
    grok.adapts(Interface, Interface, Interface,
                uvcsite.browser.layout.slots.interfaces.IPersonalMenu)

    @property
    def action(self):
        return uvcsite.getHomeFolderUrl(self.request, "++plugins++")
