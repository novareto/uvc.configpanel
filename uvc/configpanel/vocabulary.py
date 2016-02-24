# -*- coding: utf-8 -*-

from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtilitiesFor
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from .interfaces import IConfigurablePlugin


def configurable_plugins():
    plugins = SimpleVocabulary([
        SimpleTerm(token=name, title=utility.title, value=utility)
        for name, utility in getUtilitiesFor(IConfigurablePlugin)])
    return plugins
