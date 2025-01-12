from F_P2_Solution import P2_Solution as Solution
import random as rn
from copy import deepcopy

class P2_Genetic_Operator:
	def cross(self, parent_1: Solution, parent_2: Solution) -> Solution:
		instance = parent_1.get_instance()
		objetive_function = parent_1.get_objetive_function()
		self.charging_stations = instance.get_charging_stations()
		self.inicios = []
		self.medios = []
		self.finales = []
		self._get_splited_parts(parent_1)
		self._get_splited_parts(parent_2)
		rn.shuffle(self.inicios)
		rn.shuffle(self.medios)
		rn.shuffle(self.finales)
		for i in range(len(self.inicios) // 2):
			matrix = [[] for _ in range(instance.get_num_vehicle())]
			for j in range(len(matrix)):
				vehicle = matrix[j]
				vehicle += self.inicios[i + j]
				try:
					vehicle += (self.medios[i + j])
				except:
					pass
				vehicle += (self.finales[i + j])
			if objetive_function.is_valid(matrix, instance):
				sol = Solution(instance, objetive_function)
				sol.set_new_matrix(matrix)
				return sol
		return None

	def mutation(self, child: Solution) -> bool:
		matrix = deepcopy(child.get_matrix())
		rn.shuffle(matrix)
		first_vehicle = matrix[0]
		if len(matrix) - 1 > 0:
			second_vehicle = matrix[rn.randint(1, len(matrix) - 1)]
		else:
			second_vehicle = matrix[0]
		while len(first_vehicle) < 2:
			rn.shuffle(matrix)
			first_vehicle = matrix[0]
		try:
			first_index = rn.randint(1, len(first_vehicle) - 2)
		except:
			first_index = 1
		not_cancelled = True
		while first_vehicle[first_index] in child.instance.get_charging_stations() and not_cancelled:
			try:
				first_index = rn.randint(1, len(first_vehicle) - 2)
			except:
				first_index = 1
				not_cancelled = False
		try:
			second_index = rn.randint(1, len(second_vehicle) - 2)
		except:
			second_index = 1
		not_cancelled = True
		while second_vehicle[second_index] in child.instance.get_charging_stations() and not_cancelled:
			try:
				second_index = rn.randint(1, len(second_vehicle) - 2)
			except:
				second_index = 1
				not_cancelled = False
		first_vehicle[first_index], second_vehicle[second_index] = second_vehicle[second_index], first_vehicle[first_index]
		if child.objetive_function.is_valid(matrix, child.get_instance()):
			child.set_new_matrix(matrix)
			return True
		else:
			return False

	def _get_splited_parts(self, parent):
		for vehicle in parent.get_matrix():
			if len(vehicle) == 1:
				self.inicios.append([vehicle[0]])
				self.finales.append([vehicle[0]])
			elif len(vehicle) == 2:
				self.inicios.append([vehicle[0]])
				self.finales.append([vehicle[1]])
			elif len(vehicle) == 3:
				self.inicios.append([vehicle[0]])
				self.medios.append([vehicle[1]])
				self.finales.append([vehicle[2]])
			else:
				charging_indices = [
					i for i, node in enumerate(vehicle)
					if node in self.charging_stations
				]

				if len(charging_indices) < 2:
					self.inicios.append(vehicle[:1])
					self.finales.append(vehicle[-1:])
					self.medios.append([])
					continue

				first_index = charging_indices[0]
				last_index = charging_indices[-1]

				self.inicios.append(vehicle[:first_index + 1])
				self.medios.append(vehicle[first_index + 1:last_index])
				self.finales.append(vehicle[last_index:])

