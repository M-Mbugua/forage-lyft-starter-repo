from utils import add_years_to_date

from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
		self.current_date = current_date
		self.last_service_date = last_service_date

	def needs_service(self):
		date_to_service_battery_by = add_years_to_date(self.last_service_date + 3)

		if date_to_service_battery_by < self.current_date:
			return True

		else:
			return False

