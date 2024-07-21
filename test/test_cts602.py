import unittest
from common import GenvexNabtoCTS602, GenvexNabtoDatapointKey
from modelTester import modelTester

class CTS602WithNoQuirksTest(modelTester):    
    def setUp(self):
        self.loadedModel = GenvexNabtoCTS602()
        self.loadedModel.addDeviceQuirks(0,0,0) # Should not load any quirks.
        self.expectedName = "CTS 602"
        self.expectedManufacturer = "Nilan"

    def test_quirks_not_loaded(self):
        self.assertNotIn(GenvexNabtoDatapointKey.HOTWATER_TOP, self.loadedModel._datapoints)

class CTS602WithQuirksTest(modelTester):    
    def setUp(self):
        self.loadedModel = GenvexNabtoCTS602()
        self.loadedModel.addDeviceQuirks(0,0,12)
        self.expectedName = "CTS 602"
        self.expectedManufacturer = "Nilan"

    def test_hotwater_temp_quirk_loaded(self):
        self.assertIn(GenvexNabtoDatapointKey.HOTWATER_TOP, self.loadedModel._datapoints)
    

if __name__ == '__main__':
    unittest.main()