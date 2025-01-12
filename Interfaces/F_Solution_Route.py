from abc import ABC, abstractmethod
from Interfaces.F_Instance import Instance
from Utilities.F_P2_Colony import P2_Colony as Colony

class Solution_Route(ABC):

	def get_instance(self) -> Instance:
		pass

	def get_of_value(self) -> int:
		pass

	def get_matrix(self) -> list[list[Colony]]:
		pass

	def get_CPU_time(self) -> float:
		pass

	def get_percentage_improved(self) -> str:
		pass

	def set_new_matrix(self, new_matrix: list[list[Colony]]) -> None:
		pass

	def set_CPU_time(self, time):
		pass

	def set_percentage_improved(self, last_value):
		pass

	def _calculate_value(self) -> float:
		pass
