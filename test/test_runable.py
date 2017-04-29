import unittest

import sys
import time
from functools import partial
from kivy.clock import Clock

sys.path.append('../src')
from Gui import MainGUIApp

class Test(unittest.TestCase):

    def pause(*args):
        time.sleep(0.000001)

    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)
        self.assertFalse(app.root.runable())
        app.root.setstylenum(1)
        self.assertFalse(app.root.runable())
        app.root.setdownloadvalid(True)
        self.assertTrue(app.root.runable())
        app.root.setstylenum(0)
        self.assertFalse(app.root.runable())
        app.stop()

    def test_stylebuttons(self):
        app = MainGUIApp()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, 0.000001)
        app.run()

if __name__ == '__main__':
    unittest.main()