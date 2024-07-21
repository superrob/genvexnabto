from common import GenvexNabtoBaseModel, GenvexNabtoSetpointKey, GenvexNabtoDatapointKey
import sys
import unittest
import logging
logging.basicConfig( stream=sys.stderr )
logging.getLogger( "SomeTest.testSomething" ).setLevel( logging.DEBUG )
class modelTester(unittest.TestCase):

    def setUp(self):
        self.loadedModel = GenvexNabtoBaseModel()
        self.expectedName = "Basemodel"
        self.expectedManufacturer = ""

    def test_correct_name(self):
        self.assertEqual(self.expectedName, self.loadedModel.getModelName())

    def test_correct_manufacturer(self):
        self.assertEqual(self.expectedManufacturer, self.loadedModel.getManufacturer())    
    
    def test_valid_setpoint_keys(self):
        for key in self.loadedModel._setpoints:            
            currentSetpoint = self.loadedModel._setpoints[key]    
            self.assertIsNotNone(currentSetpoint["read_obj"])
            self.assertIsNotNone(currentSetpoint["read_address"])
            self.assertIsNotNone(currentSetpoint["write_obj"])
            self.assertIsNotNone(currentSetpoint["write_address"])
            self.assertIsNotNone(currentSetpoint["divider"])
            self.assertIsNotNone(currentSetpoint["min"])
            self.assertIsNotNone(currentSetpoint["max"])

            self.assertNotEqual(currentSetpoint["divider"], 0)
        
    def test_valid_datapoint_keys(self):
        for key in self.loadedModel._datapoints:
            currentDatapoint = self.loadedModel._datapoints[key]
            self.assertIsNotNone(currentDatapoint["obj"])
            self.assertIsNotNone(currentDatapoint["address"])
            self.assertIsNotNone(currentDatapoint["divider"])
            self.assertIsNotNone(currentDatapoint["offset"])

            self.assertNotEqual(currentDatapoint["divider"], 0)
        
    def test_datapoint_request_is_list(self):
        self.assertIsInstance(self.loadedModel.getDefaultDatapointRequest(), list)

    def test_valid_datapoint_request(self):
        datapointRequest = self.loadedModel.getDefaultDatapointRequest()
        for key in datapointRequest:
            self.assertIn(key, self.loadedModel._datapoints)

    def test_setpoint_request_is_list(self):
        self.assertIsInstance(self.loadedModel.getDefaultSetpointRequest(), list)

    def test_valid_setpoint_request(self):
        setpointRequest = self.loadedModel.getDefaultSetpointRequest()
        for key in setpointRequest:
            self.assertIn(key, self.loadedModel._setpoints)