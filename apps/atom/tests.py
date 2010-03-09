import unittest, os

from rapidsms.tests.scripted import TestScript
from apps.atom.models import IVRFeedParser

class FeedParserTest (unittest.TestCase):
    def setUp(self):
        path = os.path.dirname(__file__)
        path = os.path.join(path, "tests", "data", "atom.xml")
        self.file_stream = open(path, 'r')

    def test_parse_feed(self):
        parser = IVRFeedParser()
        entries = parser.parse(self.file_stream)
        self.assertEquals(len(entries), 2)

        firstEntry = entries[0]

        self.assertEquals(firstEntry.title, 'First Submission')
        self.assertEquals(firstEntry.uid, 'tag:zain.iq.com,2004-05-27:/ivr/unicef/789')
        self.assertEquals(firstEntry.updated, '2009-12-15 04:47:45')
        self.assertEquals(firstEntry.governorate, 10)
        self.assertEquals(firstEntry.district, 3)
        self.assertEquals(firstEntry.age, 6)
        self.assertEquals(firstEntry.female, True)
        self.assertEquals(firstEntry.file_url, 'http://www.zain.iq.com/ivr/unicef/data/789.mp3')

        firstEntry.save()