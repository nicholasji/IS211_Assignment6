#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Week 6 Test"""
import conversions 
import unittest 


class CelsiusToKelvin(unittest.TestCase): 


    def test_one(self): 
        results = conversions.convertCelsiusToKelvin(300)
        self.assertEqual(573.15, results)
        

    def test_two(self):
        results = conversions.convertCelsiusToKelvin(0)
        self.assertEqual(273.15, results)
        

    def test_three(self): 
        results = conversions.convertCelsiusToKelvin(-100)
        self.assertEqual(173.15, results)
        

    def test_four(self):
        results = conversions.convertCelsiusToKelvin(25.5)
        self.assertEqual(298.65, results)
        

    def test_five(self):
        results = conversions.convertCelsiusToKelvin(1000)
        self.assertEqual(1273.15, results)
        
    
class CelsiusToFahrenheit(unittest.TestCase):


    def test_one(self):
        results = conversions.convertCelsiusToFahrenheit(300)
        self.assertEqual(572.0, results)
        

    def test_two(self):
        results = conversions.convertCelsiusToFahrenheit(0)
        self.assertEqual(32.0, results)
        

    def test_three(self):
        results = conversions.convertCelsiusToFahrenheit(-100)
        self.assertEqual(-148, results)
        

    def test_four(self):
        results = conversions.convertCelsiusToFahrenheit(25.5)
        self.assertEquals(77.9, results)
        

    def test_five(self):
        results = conversions.convertCelsiusToFahrenheit(1000)
        self.assertEqual(1832, results)

class FharenheitToKelvin(unittest.TestCase): 


    def test_one(self):
        results = conversions.convertFahrenheitToKelvin(300)
        self.assertEqual(422.039, results)
        

    def test_two(self):
        results = conversions.convertFahrenheitToKelvin(0)
        self.assertEqual(255.372, results)
        

    def test_three(self):
        results = conversions.convertFahrenheitToKelvin(-100)
        self.assertEqual(199.817, results)
        

    def test_four(self):
        results = conversions.convertFahrenheitToKelvin(1000)
        self.assertEquals(810.928, results)
        

    def test_five(self):
        results = conversions.convertFahrenheitToKelvin(567890)
        self.assertEqual(315749.817, results)

class FahrenheitToCelsius(unittest.TestCase):

    def test_one(self):
        results = conversions.convertFahrenheitToCelsius(300)
        self.assertEqual(148.889, results)
        

    def test_two(self):
        results = conversions.convertFahrenheitToCelsius(0)
        self.assertEqual(-17.778, results)
        

    def test_three(self):
        results = conversions.convertFahrenheitToCelsius(-100)
        self.assertEqual(-73.333, results)
        

    def test_four(self):
        results = conversions.convertFahrenheitToCelsius(25.5)
        self.assertEquals(-3.611, results)
        

    def test_five(self):
        results = conversions.convertFahrenheitToCelsius(1000)
        self.assertEqual(537.778, results)
        
class KelvinToCelsius(unittest.TestCase):

    def test_one(self):
        results = conversions.convertKelvinToCelsius(300)
        self.assertEqual(26.85, results)
        

    def test_two(self):
        results = conversions.convertKelvinToCelsius(0)
        self.assertEqual(-273.15, results)
        

    def test_three(self):
        results = conversions.convertKelvinToCelsius(-100)
        self.assertEqual(-373.15, results)
        

    def test_four(self):
        results = conversions.convertKelvinToCelsius(25.5)
        self.assertEquals(-247.65, results)
        

    def test_five(self):
        results = conversions.convertKelvinToCelsius(1000)
        self.assertEqual(726.85, results)
        
class KelvinToFahrenheit(unittest.TestCase):
    

    def test_one(self):
        results = conversions.convertKelvinToFahrenheit(300)
        self.assertEqual(80.33, results)
        

    def test_two(self):
        results = conversions.convertKelvinToFahrenheit(0)
        self.assertEqual(-459.67, results)
        

    def test_three(self):
        results = conversions.convertKelvinToFahrenheit(-100)
        self.assertEqual(-639.67, results)
        

    def test_four(self):
        results = conversions.convertKelvinToFahrenheit(25.5)
        self.assertEquals(-413.77, results)
        

    def test_five(self):
        results = conversions.convertKelvinToFahrenheit(1000)
        self.assertEqual(1340.33, results)

if __name__ == "__main__":
    unittest.main()
