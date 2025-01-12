from abc import ABC, abstractmethod
from Interfaces.F_Instance import Instance
from Interfaces.F_Objetive_Function import Objetive_Function
from Interfaces.F_Solution_Route import Solution_Route

class Experiment(ABC):

	@abstractmethod
	def run(self, instance: Instance, objetive_function: Objetive_Function) -> Solution_Route:
		pass
