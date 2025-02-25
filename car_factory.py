from car import Car

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

from tyres.carrigan_tyres import CarriganTyres
from tyres.octoprime_tyres import OctoprimeTyres


class CarFactory:
	@staticmethod
	def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear):
		engine = CapuletEngine(current_mileage, last_service_mileage)
		battery = SpindlerBattery(current_date, last_service_date)
		tyres = CarriganTyres(tyre_wear)
		car = Car(engine, battery, tyres)
		return car 


	@staticmethod
	def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear):
		engine = WilloughbyEngine(current_mileage, last_service_mileage)
		battery = SpindlerBattery(current_date, last_service_date)
		tyres = OctoprimeTyres(tyre_wear)
		car = Car(engine, battery, tyres)
		return car 


	@staticmethod
	def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear):
		engine = SternmanEngine(current_mileage, last_service_mileage)
		battery = NubbinBattery(current_date, last_service_date)
		tyres = CarriganTyres(tyre_wear)
		car = Car(engine, battery, tyres)
		return car 


	@staticmethod
	def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear):
		engine = WilloughbyEngine(current_mileage, last_service_mileage)
		battery = NubbinBattery(current_date, last_service_date)
		tyres = OctoprimeTyres(tyre_wear)
		car = Car(engine, battery, tyres)
		return car 


	@staticmethod
	def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear):
		engine = CapuletEngine(current_mileage, last_service_mileage)
		battery = NubbinBattery(current_date, last_service_date)
		tyres = CarriganTyres(tyre_wear)
		car = Car(engine, battery, tyres)
		return car
