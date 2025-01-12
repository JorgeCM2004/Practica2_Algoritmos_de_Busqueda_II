from abc import ABC, abstractmethod
from Utilities.F_P2_Colony import P2_Colony as Colony
from Interfaces.F_Solution_Route import Solution_Route
from Interfaces.F_Instance import Instance

class Objetive_Function(ABC):

	@abstractmethod
	def evaluate(self, solution: Solution_Route, instance: Instance) -> float:
		pass

	def is_valid(self, matrix: list[list[Colony]], instance: Instance) -> bool:
		pass
