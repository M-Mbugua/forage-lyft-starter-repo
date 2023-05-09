from abc import ABC

from car import Car

from engines.engine import Engine

class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False