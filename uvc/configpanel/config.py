# -*- coding: utf-8 -*-

import grok


import uvcsite.browser.layout.menu
from uvcsite.interfaces import IHomeFolder
import uvcsite.browser.layout.slots.interfaces


class MyPrefsMenu(uvcsite.browser.layout.menu.MenuItem):
    grok.name("my_prefs_menu")
    grok.title(u"Erweiterte Einstellungen")
    grok.require('uvc.ManageCoUsers')
    uvcsite.browser.layout.menu.menu(
        uvcsite.browser.layout.slots.interfaces.IPersonalMenu
    )

    title = u"Erweiterte Einstellungen"
    icon = "fas fa-wrench"

    def url(self):
        return self.view.url(IHomeFolder(self.request.principal), "++plugins++")
