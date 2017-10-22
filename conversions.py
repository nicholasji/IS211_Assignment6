#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 6"""


def convertCelsiusToKelvin(temp):
    conversion = temp + 273.15
    return float("%.3f" % conversion)
    

def convertCelsiusToFahrenheit(temp):
    conversion = (1.8 * temp) + 32
    return float("%.3f" % conversion)


def convertFahrenheitToKelvin(temp):
    conversion = ((temp - 32) / 1.8) + 273.15
    return float("%.3f" % conversion)


def convertFahrenheitToCelsius(temp):
    conversion = (temp - 32) / 1.8
    return float("%.3f" % conversion)


def convertKelvinToCelsius(temp):
    conversion = temp - 273.15
    return float("%.3f" % conversion)
    

def convertKelvinToFahrenheit(temp):
    conversion = (temp - 273.15) * 1.8 + 32
    return float("%.3f" % conversion)
