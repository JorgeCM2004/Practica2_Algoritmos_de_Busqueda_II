from Interfaces.F_Solution_Route import Solution_Route
from Interfaces.F_Instance import Instance
from Interfaces.F_Objetive_Function import Objetive_Function
from Utilities.F_P2_Colony import P2_Colony as Colony

class P2_Solution(Solution_Route):
	def __init__(self, instance: Instance, objetive_function: Objetive_Function) -> None:
		self.instance = instance
		self.objetive_function = objetive_function
		self.value = None

	def __lt__(self, other: 'P2_Solution'):
		if self.value is None and (other is None or other.value is None):
			return False
		if self.value is None:
			return False
		if other is None or other.value is None:
			return True
		return self.value < other.value

	def __str__(self):
		return self.transformed_solution

	def get_instance(self) -> Instance:
		return self.instance

	def get_objetive_function(self) -> Objetive_Function:
		return self.objetive_function

	def get_of_value(self) -> int:
		return self.value

	def get_matrix(self) -> list[list[Colony]]:
		try:
			return self.matrix
		except:
			return None

	def get_CPU_time(self) -> float:
		try:
			return self.CPU_time
		except:
			raise ValueError("No se ha establecido el tiempo de CPU.")

	def set_new_matrix(self, new_matrix: list[list[Colony]]) -> None:
		self.matrix = new_matrix
		self.value = self._calculate_value()
		self._transform_solution()

	def set_CPU_time(self, time):
		self.CPU_time = time

	def set_algorithm(self, string):
		self.algorithm_name = string

	def _calculate_value(self) -> float:
		return self.objetive_function.evaluate(self.matrix, self.instance)

	def _transform_solution(self) -> str:
		try:
			self.matrix
		except:
			raise ValueError("No se ha establecido la matriz de colonias.")
		self.transformed_solution = "\""
		for i in range(len(self.matrix)):
			vehicle = self.matrix[i]
			self.transformed_solution += '['
			for j in range(len(vehicle)):
				self.transformed_solution += str(vehicle[j].get_name())
				if j < len(vehicle) - 1:
					self.transformed_solution += ', '
			self.transformed_solution += ']'
			if i < len(self.matrix) - 1:
				self.transformed_solution += '; '
		self.transformed_solution += "\""
