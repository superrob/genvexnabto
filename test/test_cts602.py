import unittest
from common import GenvexNabtoCTS602, GenvexNabtoCTS602Light, GenvexNabtoDatapointKey
from modelTester import modelTester

class CTS602WithNoQuirksTest(modelTester):    
    def setUp(self):
        self.loadedModel = GenvexNabtoCTS602(0)
        self.loadedModel.addDeviceQuirks() # Should not load any quirks.
        self.expectedName = "CTS 602 - Unknown model"
        self.expectedManufacturer = "Nilan"
        self.loadedModel.finishLoading()
        
    def test_if_device_has_quirk(self):
        self.assertFalse(self.loadedModel.deviceHasQuirk("heatpumpData", 0))

    def test_has_quirk_with_invalid_quirk(self):
        self.assertFalse(self.loadedModel.deviceHasQuirk("thisIsInvalid", 0))

    def test_quirks_not_loaded(self):
        self.assertNotIn(GenvexNabtoDatapointKey.HOTWATER_TOP, self.loadedModel._datapoints)

class CTS602WithExtractTempSensor(modelTester):    
    def setUp(self):
        self.loadedModel = GenvexNabtoCTS602(13)
        self.loadedModel.addDeviceQuirks()
        self.expectedName = "CTS 602 - Comfort"
        self.expectedManufacturer = "Nilan"
        self.loadedModel.finishLoading()

    def test_extract_sensor_used(self):
        self.assertEqual(self.loadedModel._datapoints[GenvexNabtoDatapointKey.TEMP_EXTRACT]['address'], 34)

class CTS602WithQuirksTest(modelTester):    
    def setUp(self):
        self.loadedModel = GenvexNabtoCTS602(12)
        self.loadedModel.addDeviceQuirks()
        self.expectedName = "CTS 602 - VP18cCompact"
        self.expectedManufacturer = "Nilan"
        self.loadedModel.finishLoading()

    def test_hotwater_temp_quirk_loaded(self):
        self.assertTrue(self.loadedModel.modelProvidesDatapoint(GenvexNabtoDatapointKey.HOTWATER_TOP))

class CTS602WithHPSQuirksTest(modelTester):    
    def setUp(self):
        self.loadedModel = GenvexNabtoCTS602(144)
        self.loadedModel.addDeviceQuirks()
        self.expectedName = "CTS 602 - Compact P AIR"
        self.expectedManufacturer = "Nilan"
        self.loadedModel.finishLoading()

    def test_if_device_has_quirk(self):
        self.assertTrue(self.loadedModel.deviceHasQuirk("heatpumpData", 144))

    def test_hotwater_temp_quirk_loaded(self):        
        self.assertTrue(self.loadedModel.modelProvidesDatapoint(GenvexNabtoDatapointKey.HPS_HEATER_ACTIVE))   
    
class CTS602Light(modelTester):    
    def setUp(self):
        self.loadedModel = GenvexNabtoCTS602Light(0)
        self.expectedName = "CTS 602light"
        self.expectedManufacturer = "Nilan"
        self.loadedModel.finishLoading()

if __name__ == '__main__':
    unittest.main()