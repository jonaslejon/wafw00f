#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Barikode (Ethic Ninja)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<strong>barikode</strong>'),
    ]
    if any(i for i in schemes):
        return True
    return False