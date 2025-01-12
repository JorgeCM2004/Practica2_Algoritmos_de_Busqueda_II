from Interfaces.F_Objetive_Function import Objetive_Function
from Interfaces.F_Instance import Instance
from Utilities.F_P2_Colony import P2_Colony as Colony

class P2_Objetive_Function(Objetive_Function):
	def evaluate(self, matrix: list[list[Colony]], instance: Instance) -> float:
		val = 0
		for vehicle in matrix:
			for i in range(len(vehicle) - 1):
				val += instance(vehicle[i], vehicle[i + 1])
		return val

	def is_valid(self, matrix: list[list[Colony]], instance: Instance) -> bool:
		visited_colonies = []
		energy_factor = instance.get_energy_factor()
		for vehicle in matrix:
			if vehicle[0] != vehicle[-1] or vehicle[0] != instance.get_central_station():
				return False
			battery = instance.get_battery()
			capacity = instance.get_capacity()
			for i in range(len(vehicle) - 1):
				distance = instance(vehicle[i], vehicle[i + 1])
				battery -= distance * energy_factor
				if battery < 0:
					return False
				if vehicle[i + 1] in visited_colonies:
					return False
				if vehicle[i + 1].demand > 0:
					visited_colonies.append(vehicle[i + 1])
					capacity -= vehicle[i + 1].demand
					if capacity < 0:
						return False
				else:
					battery = instance.get_battery()
		return len(visited_colonies) + 1 == instance.get_dimension()
