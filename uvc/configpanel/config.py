# -*- coding: utf-8 -*-

import grok
import uvcsite


class MyPrefsMenu(uvcsite.MenuItem):
    grok.title(u'Erweiterte Einstellungen')
    grok.require('uvc.ManageCoUsers')
    grok.viewletmanager(uvcsite.IPersonalMenu)

    @property
    def action(self):
        return uvcsite.getHomeFolderUrl(self.request, "++plugins++")
