#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6"""

import unittest

class ConversionNotPossible(Exception):
    pass

distance = {'met': {'yar':(0,1.09361,0),'mil':(0,0.000621371,0)},'yar': {'mil':(0,0.000568182,0),'met':(0,0.9144,0)},'mil': {'met':(0,1609.34,0),'yar':(0,1760,0)}}
temp = {'kel':{'cel':(0,1,-273.15),'fah':(-273.15,9/5,32)},'cel':{'kel':(0,1,273.15),'fah':(0,9/5,32)},'fah':{'kel':(-32,5.0/9.0,273.15),'cel':(-32,5.0/9.0,0)}}

def conversion(funit, tunit, value):
    
    funit = funit[0:3]
    tunit = tunit[0:3]
    if not ((funit in distance and tunit in distance
             ) or (funit in temp and tunit in temp)):
        raise ConversionNotPossible
    else:
        if funit == tunit:
            ret_val = value
        elif funit in distance:
            ret_val = (
                (value + distance[funit][tunit][0])
                * distance[funit][tunit][1]
                + distance[funit][tunit][2]
                )
        else:
            ret_val = (
                (value + temp[funit][tunit][0])
                * temp[funit][tunit][1]
                + temp[funit][tunit][2])

    return float("%0.2f" %ret_val)


class ConvertTests(unittest.TestCase):

    def testTemperature(self):
        self.assertEqual(conversion('celsius','fahrenheit',0),32.0)
        self.assertEqual(conversion('celsius','kelvin',0),273.15)
        self.assertEqual(conversion('kelvin','fahrenheit',0),-241.15)
        self.assertEqual(conversion('kelvin','celcius',273.15),0.0)
        self.assertEqual(conversion('fahrenheit','celcius',32),0.0)
        self.assertEqual(conversion('fahrenheit','kelvin',0),255.37)

    def testDistance(self):
        self.assertEqual(conversion('meter','mile',100),0.06)
        self.assertEqual(conversion('meter','yard',10),10.94)
        self.assertEqual(conversion('mile','meter',10),16093.4)
        self.assertEqual(conversion('mile','yard',10),17600.00)
        self.assertEqual(conversion('yard','meter',3),2.74)
        self.assertEqual(conversion('yard','mile',300),0.17)

    def testSelf(self):
        for test in distance:
            self.assertEqual(conversion(test, test, 10), 10)
        for test in temp:
            self.assertEqual(conversion(test, test, 10), 10)

    def testErrors(self):
        self.assertRaises(ConversionNotPossible,conversion,'met','cel',0)

if __name__ == '__main__':
    unittest.main()
