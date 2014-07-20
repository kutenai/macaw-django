from __future__ import absolute_import

from os.path import dirname,join
import unittest
import yaml
from watchdog.events import FileCreatedEvent,EVENT_TYPE_CREATED

from ..templates import MacawHandler

class TestMacawHandler(unittest.TestCase):

    def setUp(self):
        self.yaml = """
index.html:
  class: topbar

  template: topbar.html

  prefix: |
    {% load url from future %}
    {% load staticfiles %}
    {% load i18n %}

        """
        self.specs = yaml.load(self.yaml)
        self.seq = range(10)

    def test_created(self):

        base = dirname(__file__)
        testfile = join(base,'index.html')

        h = MacawHandler(specs=self.specs,
                         designbase=base,templatebase=base)
        evt = FileCreatedEvent(testfile)
        h.on_created(evt)





if __name__ == '__main__':
    unittest.main()
