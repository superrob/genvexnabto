import unittest
from common import GenvexNabtoOptima250, GenvexNabtoOptima251, GenvexNabtoOptima260, GenvexNabtoOptima270, GenvexNabtoOptima301, GenvexNabtoOptima312, GenvexNabtoOptima314
from modelTester import modelTester

class Optima250Test(modelTester):    
    def setUp(self):
        self.loadedModel = GenvexNabtoOptima250()
        self.expectedName = "Optima 250"
        self.expectedManufacturer = "Genvex"

class Optima251Test(modelTester):    
    def setUp(self):
        self.loadedModel = GenvexNabtoOptima251()
        self.expectedName = "Optima 251"
        self.expectedManufacturer = "Genvex"

class Optima260Test(modelTester):
    def setUp(self):
        self.loadedModel = GenvexNabtoOptima260()
        self.expectedName = "Optima 260"
        self.expectedManufacturer = "Genvex"

class Optima270Test(modelTester):
    def setUp(self):
        self.loadedModel = GenvexNabtoOptima270()
        self.expectedName = "Optima 270"
        self.expectedManufacturer = "Genvex"

class Optima301Test(modelTester):
    def setUp(self):
        self.loadedModel = GenvexNabtoOptima301()
        self.expectedName = "Optima 301"
        self.expectedManufacturer = "Genvex"

class Optima312Test(modelTester):
    def setUp(self):
        self.loadedModel = GenvexNabtoOptima312()
        self.expectedName = "Optima 312"
        self.expectedManufacturer = "Genvex"

class Optima314Test(modelTester):
    def setUp(self):
        self.loadedModel = GenvexNabtoOptima314()
        self.expectedName = "Optima 314"
        self.expectedManufacturer = "Genvex"

if __name__ == '__main__':
    unittest.main()