import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-06-11")
        last_service_date = date.fromisoformat("2018-06-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2022-06-11")
        last_service_date = date.fromisoformat("2019-06-11")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-06-11")
        last_service_date = date.fromisoformat("2020-06-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2022-06-11")
        last_service_date = date.fromisoformat("2021-06-11")
        battery = SpindlerBattery(current_date, last_service_date)