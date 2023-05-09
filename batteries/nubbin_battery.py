from abc import ABC

from datetime import datetime

from batteries.battery import Battery

class NubbinEngine(Car, ABC)
    def __init__(self, current, last_service_date):
		self.current_date = current_date
		self.last_service_date = last_service_date

	def needs_service(self):
		difference = datetime(self.current_date, self.last_service_date)
		return (difference.year >= 4)