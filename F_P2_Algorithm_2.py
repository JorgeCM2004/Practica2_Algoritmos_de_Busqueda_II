from Interfaces.F_Instance import Instance
from Interfaces.F_Objetive_Function import Objetive_Function
from Algorithms.F_P2_Ant import P2_Ant as Ant
from Algorithms.F_P2_Genetic_Operator import P2_Genetic_Operator as Genetic_Operator
from time import time
import random as rn

class P2_Algorithm_2:
	"""
	Genetic Algorithm
	"""
	def run(self, instance: Instance, objetive_function: Objetive_Function, max_time: float, matting_pool_size = 100, cross_probability: float = 0.9, mutation_probability: float = 1):
		time0 = time()
		time1 = time0
		ant = Ant(instance, objetive_function)
		genetic = Genetic_Operator()
		false_pheromones = self._initialize_pheromones(instance, 1)
		matting_pool = []
		best_sol = None
		for _ in range(matting_pool_size):
			new_sol = ant.explore(false_pheromones, 1, 1)
			if new_sol.get_of_value() is not None:
				new_sol.set_algorithm("Algorithm_1")
				matting_pool.append(new_sol)
				if new_sol < best_sol:
					best_sol = new_sol
		while time1 - time0 < max_time or best_sol is None:
			rn.shuffle(matting_pool)
			for i in range(0, len(matting_pool) - 1, 2):
				if rn.random() <= cross_probability:
					higher = max((matting_pool[i].get_of_value(), i), (matting_pool[i + 1].get_of_value(), i + 1))
					new_sol = genetic.cross(matting_pool[i], matting_pool[i + 1])
					if new_sol is not None:
						new_sol.set_algorithm("Algorithm_2")
						if rn.random() <= mutation_probability:
							mutated = genetic.mutation(new_sol)
						if new_sol < best_sol:
							best_sol = new_sol
						matting_pool[higher[1]] = new_sol
			time1 = time()
		return best_sol

	def _initialize_pheromones(self, instance: Instance, q: int) -> None:
		return [[q for _ in range(instance.get_number_of_nodes())] for _ in range(instance.get_number_of_nodes())]
