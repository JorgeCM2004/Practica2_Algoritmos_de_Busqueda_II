from typing import Literal
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from F_P2_Runner import P2_Runner

TIME = 10

class P2_Tests:
	def __init__(self) -> None:
		self.expected_quality = []
		self._fill_quality()

	def get_number_of_tests(self):
		return len(self.expected_quality)

	def get_number_of_instances(self):
		return self.num_instances

	def run_test(self, algorithm: Literal["Algorithm_1", "Algorithm_2"]):
		runner = P2_Runner()
		runner.run(algorithm, TIME, save=True)
		solution_list: list = runner.solutions
		self.num_instances = len(solution_list)
		for instance_name_test, minimum_quality in self.expected_quality:
			i = 0
			instance_name_sol = solution_list[i].get_instance().name
			value = solution_list[i].get_of_value()
			while i < len(solution_list) and instance_name_sol != instance_name_test:
				i += 1
				instance_name_sol = solution_list[i].get_instance().name
				value = solution_list[i].get_of_value()
			if instance_name_sol == instance_name_test:
				assert minimum_quality >= value
			else:
				print("La instancia deseada no se encuentra en la carpeta de instancias.")
				assert instance_name_sol == instance_name_test


	def _fill_quality(self):
		self.expected_quality.append(("instancia_00.txt", 245.7))
		self.expected_quality.append(("instancia_01.txt", 484.41))
		self.expected_quality.append(("instancia_03.txt", 807.04))
		self.expected_quality.append(("instancia_05.txt", 1122.45))
		self.expected_quality.append(("instancia_07.txt", 2349.78))
