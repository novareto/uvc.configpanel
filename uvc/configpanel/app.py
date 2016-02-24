import grok
import uvcsite

class Index(uvcsite.Page):
    grok.context(uvcsite.IUVCSite)

    def render(self):
        return "CPANEL"


from uvc.tbskin.resources import TBSkinViewlet


class TBSkinViewlet(TBSkinViewlet):
    pass

