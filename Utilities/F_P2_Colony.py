class P2_Colony:
	def __init__(self, name: str, index: int, coordinates: tuple[float]) -> None:
		self.name = name
		self.index = index
		self.coordinates = coordinates

	def __call__(self) -> int:
		return self.index

	def __eq__(self, other: 'P2_Colony') -> bool:
		return self.name == other.name

	def set_demand(self, demand: int) -> None:
		self.demand = demand

	def get_demand(self) -> int:
		return self.demand

	def get_name(self) -> str:
		return self.name
