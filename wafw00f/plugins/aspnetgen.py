#!/usr/bin/env python
'''
Copyright (C) 2019, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ASP.NET Generic Protection (Microsoft)'


def is_waf(self):
    schemes = [
        self.matchContent(r'iis.(\d+.)+?detailed.error|potentially.dangerous.request.querystring|application.error.from.being.viewed.remotely.(for.security.reasons)?|An.application.error.occurred.on.the.server'),
    ]
    if any(i for i in schemes):
        return True
    return False