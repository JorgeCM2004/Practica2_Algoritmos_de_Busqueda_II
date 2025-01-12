from time import time

from Interfaces.F_Experiment import Experiment
from Interfaces.F_Instance import Instance
from Interfaces.F_Objetive_Function import Objetive_Function
from Interfaces.F_Solution_Route import Solution_Route
from Algorithms.F_P2_Ant import P2_Ant as Ant

class P2_Algorithm_1(Experiment):
	"""
	Ant Colony Optimization (ACO).
	"""
	def run(self, instance: Instance, objetive_function: Objetive_Function, max_time: float, num_ants: int = 50, alpha: float = 2, beta: float = 1, p: float = 0.3, q: int = 1, Q: float = 200) -> Solution_Route:
		time0 = time()
		time1 = time0
		self._initialize_pheromones(instance, q)
		best_sol = None
		ant = Ant(instance, objetive_function)
		while time1 - time0 < max_time or best_sol is None:
			solutions = []
			for _ in range(num_ants):
				solution = ant.explore(self.pheromones, alpha, beta)
				solution.set_algorithm("Algorithm_1")
				solutions.append(solution)
				if solution < best_sol:
					best_sol = solution
			self._update_pheromones(instance, solutions, p, Q)
			time1 = time()
		return best_sol

	def _initialize_pheromones(self, instance: Instance, q: int) -> None:
		self.pheromones = [[q for _ in range(instance.get_number_of_nodes())] for _ in range(instance.get_number_of_nodes())]

	def _update_pheromones(self, instance: Instance, solutions: list[Solution_Route], p: float, Q: float) -> None:
		for i in range(instance.get_number_of_nodes()):
			for j in range(instance.get_number_of_nodes()):
				self.pheromones[i][j] *= p
		for solution in solutions:
			if solution is not None and solution.get_matrix():
				for route in solution.get_matrix():
					for i in range(len(route) - 1):
						self.pheromones[route[i]()][route[i + 1]()] += Q / solution.get_of_value()
