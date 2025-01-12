from Interfaces.F_Instance import Instance
from Interfaces.F_Objetive_Function import Objetive_Function
from Utilities.F_P2_Colony import P2_Colony as Colony
from Utilities.F_P2_Roulette import P2_Roulette as Roulette
from F_P2_Solution import P2_Solution as Solution

EPSILON = 1e-10

class P2_Ant:
	def __init__(self, instance: Instance, objetive_function: Objetive_Function):
		self.instance = instance
		self.objetive_function = objetive_function
		self.roulette = Roulette()

	def explore(self, pheromones: list[list[float]], alpha: float, beta: float) -> None:
		matrix_sol: list[list[Colony]] = []
		nodes_to_visit = self.instance.get_colonies_to_visit()
		charging_stations = self.instance.get_charging_stations()
		num_vehicles = self.instance.get_num_vehicle()
		energy_factor = self.instance.get_energy_factor()
		for _ in range(num_vehicles):
			vehicle_capacity = self.instance.get_capacity()
			vehicle_battery = self.instance.get_battery()
			matrix_sol.append([])
			actual_node = self.instance.get_central_station()
			finished = False
			while not finished:
				if actual_node in charging_stations:
					vehicle_battery = self.instance.get_battery()
				vehicle_capacity -= actual_node.get_demand()
				feaseable_moves = []
				possible_capacity = False
				for node in nodes_to_visit:
					possible_distance = False
					for charge_node in charging_stations:
						if (self.instance(actual_node, node) + self.instance(node, charge_node)) * energy_factor<= vehicle_battery:
							possible_distance = True
					if node.get_demand() <= vehicle_capacity:
						possible_capacity = True
					if actual_node != node and node.get_demand() <= vehicle_capacity and possible_distance:
						feaseable_moves.append(node)
				if not possible_capacity and actual_node == self.instance.get_central_station():
					finished = True
					matrix_sol[-1].append(actual_node)
					break
				if not feaseable_moves:
					if not possible_capacity:
						if self.instance(actual_node, self.instance.get_central_station()) * energy_factor <= vehicle_battery:
							feaseable_moves.append(self.instance.get_central_station())
							all_charge = False
						else:
							all_charge = True
					else:
						all_charge = True
					if all_charge:
						for node in charging_stations:
							if actual_node != node and self.instance(actual_node, node) * energy_factor <= vehicle_battery:
								feaseable_moves.append(node)
				probabilities: list[float] = []
				total = 0
				for node in feaseable_moves:
					prob = pheromones[actual_node()][node()] ** alpha * (1 / (self.instance(actual_node, node) + EPSILON)) ** beta
					probabilities.append(prob)
					total += prob
				probabilities = [prob / total for prob in probabilities]
				next_node = self.roulette.spin(feaseable_moves, probabilities)
				vehicle_battery -= self.instance(actual_node, next_node) * energy_factor
				if actual_node not in charging_stations:
					nodes_to_visit.remove(actual_node)
				matrix_sol[-1].append(actual_node)
				actual_node = next_node
		sol = Solution(self.instance, self.objetive_function)
		if self.objetive_function.is_valid(matrix_sol, self.instance):
			sol.set_new_matrix(matrix_sol)
		return sol
