#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'BulletProof Security Pro (AITpro Security)'


def is_waf(self):
    schemes = [
        self.matchContent(r'If you arrived here due to a search or clicking on a link click your Browser\'s back button to return to the previous page')
    ]
    if any(i for i in schemes):
        return True
    return False