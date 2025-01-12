from abc import ABC, abstractmethod

class Instance(ABC):
	@abstractmethod
	def __call__(self, index0: int, index1: int) -> float:
		pass

	def get_num_vehicle(self) -> int:
		pass

	def get_dimension(self) -> int:
		pass

	def get_charging_stations(self) -> list:
		pass

	def get_capacity(self) -> int:
		pass

	def get_battery(self) -> int:
		pass

	def get_energy_factor(self) -> float:
		pass

	def get_optimal_value(self) -> float:
		pass
