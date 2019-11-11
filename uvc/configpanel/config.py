# -*- coding: utf-8 -*-

import grok


from uvc.menus.components import MenuItem
from uvc.menus.directives import menu 
from uvcsite.interfaces import IHomeFolder
import uvcsite.browser.layout.slots.interfaces


class MyPrefsMenu(MenuItem):
    grok.name("my_prefs_menu")
    grok.title(u"Erweiterte Einstellungen")
    #grok.require('uvc.ManageCoUsers')
    menu(
        uvcsite.browser.layout.slots.interfaces.IPersonalMenu
    )

    title = u"Erweiterte Einstellungen"
    icon = "fas fa-wrench"

    def url(self):
        return self.view.url(IHomeFolder(self.request.principal), "++plugins++")
