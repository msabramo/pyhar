#!/usr/bin/env python
from datetime import datetime

class WebObject(object):
    def __init__(self, name, version, comment=None):
        self.name = name
        self.version = version
        self.comment = comment
        
class WebSessionCreator(WebObject):
    pass

class WebSessionBrowser(WebObject):
    pass

class WebPage(object):
    def __init__(self, id, startedDateTime=None):
        self.id = id
        self.startedDateTime = startedDateTime or datetime.now()
        self.title = None
        self.comment = None

class WebEntry(object):
    def __init__(self, pageref, time, startedDateTime, url):
        self.pageref = pageref
        self.time = time
        self.startedDateTime = startedDateTime
        self.url = url

class WebSession(object):
    def __init__(self):
        self.creator = None
        self.browser = None
        self.pages = {}
        self.entries = {}
        self.comment = None
