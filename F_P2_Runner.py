from typing import Literal
from time import time

from F_P2_Search_Instances import P2_Search_Instances as Search_Instances
from F_P2_Objetive_Function import P2_Objetive_Function as Objetive_Function
from F_P2_Algorithm_1 import P2_Algorithm_1 as Algorithm_1
from F_P2_Algorithm_2 import P2_Algorithm_2 as Algorithm_2
from Utilities.F_P2_Saver import P2_Saver as Saver

class P2_Runner:
	def __init__(self):
		self.searcher = Search_Instances()
		self.objetive_function = Objetive_Function()

	def run(self, algorithm_name: Literal["Algorithm_1", "Algorithm_2"], seconds_per_instance: int, save: bool) -> None:
		seconds_per_instance = seconds_per_instance * 0.95
		if algorithm_name == "Algorithm_1":
			algorithm = Algorithm_1()
		elif algorithm_name == "Algorithm_2":
			algorithm = Algorithm_2()
		else:
			raise ValueError("El nombre del algoritmo no es valido.")
		solutions = []
		for instance in self.searcher:
			seconds = instance.get_number_of_nodes() * seconds_per_instance * len(self.searcher.instances_list) / self.searcher.total_unit
			time0 = time()
			solution = algorithm.run(instance, self.objetive_function, seconds)
			solution.set_CPU_time(time() - time0)
			solutions.append(solution)
		self.solutions = solutions
		if save:
			saver = Saver()
			saver.save(solutions)
