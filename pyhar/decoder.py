#!/usr/bin/env python
import re
from datetime import datetime, timedelta
    
from session import WebEntry, WebPage, WebSession, WebSessionCreator, WebSessionBrowser

class HARDecodeError(ValueError):
    def __init__(self, msg):
        ValueError.__init__(self, msg)

class HARDecoder(object):
    RE_DATETIME = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})T" \
                             r"(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})\." \
                             r"(?P<ms>\d{3})(?P<zone_sign>[\+-])(?P<zone_hour>\d{2}):(?P<zone_minute>\d{2})")
    
    def __init__(self, encoding='utf-8', *kwds):
        self.encoding = encoding
        
    def _assertProperty(self, obj, names):
        for name in names:
            if name not in obj:
                raise HARDecodeError("Expecting `%s` object" % name)
        
    def _decodeWebObject(self, obj, cls, optional=True):
        self._assertProperty(obj, ['name', 'version'])
            
        return cls(obj['name'], obj['version'], obj.get('comment'))
    
    def _decodeWebPage(self, obj):
        self._assertProperty(obj, ['startedDateTime', 'id', 'title'])
        
        page = WebPage(obj['id'], self._decodeDatetime(obj['startedDateTime']))
        page.title = obj['title']
        page.comment = obj.get('comment')
                
        return page
    
    def _decodeWebEntry(self, obj):
        self._assertProperty(obj, ['pageref', 'time', 'startedDateTime'])
        
        return WebEntry(obj['pageref'], obj['time'], obj['startedDateTime'], obj['request']['url'])
    
    def _decodeDatetime(self, s):
        m = self.RE_DATETIME.match(s)
        
        if m:
            zone_sign = 1 if m.group('zone_sign') == '+' else -1
            td = timedelta(hours=zone_sign*int(m.group('zone_hour')), minutes=zone_sign*int(m.group('zone_minute')))
            
            return datetime(int(m.group('year')), int(m.group('month')), int(m.group('day')),
                            int(m.group('hour')), int(m.group('minute')), int(m.group('second')),
                            int(m.group('ms'))) + td
        
        raise HARDecodeError('Fail to decode datetime: %s' % s)
        
    def decode(self, obj):
        session = WebSession()
        
        self._assertProperty(obj, ['log'])
            
        log = obj['log']
        
        version = log.get('version') or '1.1'
        
        self._assertProperty(log, ['creator', 'entries'])
        
        session.creator = self._decodeWebObject(log.get('creator'), WebSessionCreator)
        session.browser = self._decodeWebObject(log.get('browser'), WebSessionBrowser) if 'browser' in log else None
        
        if 'pages' in log:
            pages = [self._decodeWebPage(page) for page in log['pages']]
            session.pages = dict([(page.id, page) for page in pages])
            
        entries = [self._decodeWebEntry(entry) for entry in log['entries']]
        session.entries = dict([(entry.url, entry) for entry in entries])
        
        session.comment = log.get('comment')
        
        return session

