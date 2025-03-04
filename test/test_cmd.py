import unittest
from common import GenvexCommandPing, GenvexCommandKeepAlive

class cmdTester(unittest.TestCase):
    def setUp(self):
        self.cmd_ping = GenvexCommandPing()
        self.cmd_keepalive = GenvexCommandKeepAlive()
        
    def test_ping_builder(self):
        self.assertEqual(self.cmd_ping.buildCommand(), b'\x00\x00\x00\x11\x70\x69\x6e\x67')

    def test_keepalive_builder(self):
        self.assertEqual(self.cmd_keepalive.buildCommand(), b'\x00\x00\x00\x02')

if __name__ == '__main__':
    unittest.main()