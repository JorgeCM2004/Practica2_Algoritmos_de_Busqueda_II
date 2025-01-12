from typing import Literal

from Utilities.F_P2_Colony import P2_Colony as Colony

class P2_Distance_Calculator:
	def __init__(self, formula_name: Literal["Euclidean", "Manhattan"] = "Euclidean") -> None:
		self.formulas_dict = {"Euclidean": self._euclidean_distance, "Manhattan": self._manhattan_distance}
		self.formula = self.formulas_dict[formula_name]

	def __call__(self, c1: Colony, c2: Colony, new_formula: Literal["Euclidean", "Manhattan"] = None) -> float:
		if new_formula is not None:
			self.formula = self.formulas_dict[new_formula]
		return self.formula(c1.coordinates, c2.coordinates)

	def _euclidean_distance(self, coords1: tuple[float], coords2: tuple[float]) -> float:
		return ((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2)**0.5

	def _manhattan_distance(self, coords1: tuple[float], coords2: tuple[float]) -> float:
		return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])
