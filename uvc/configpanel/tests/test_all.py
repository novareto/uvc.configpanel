# -*- coding: utf-8 -*-

import doctest
import unittest
from grokcore.component import testing


def setUp(test):
    testing.grok('zeam.form.ztk')
    testing.grok('uvc.configpanel')


def test_suite():
    optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    globs = {}

    suite = unittest.TestSuite()
    for filename in ['component.txt']:
        test = doctest.DocFileSuite(
            filename,
            setUp=setUp,
            optionflags=optionflags,
            globs=globs)
        suite.addTest(test)

    return suite
