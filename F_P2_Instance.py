from Interfaces.F_Instance import Instance
from Utilities.F_P2_Colony import P2_Colony as Colony
from Utilities.F_P2_Distance_Calculator import P2_Distance_Calculator as Distance_Calculator

class P2_Instance(Instance):
	def __init__(self, route: str):
		self.route = route
		self.colony_names: list[str] = []
		self.colonies_to_visit: list[Colony] = []
		self.charging_stations: list[Colony] = []
		self.colony_list: dict[str, Colony] = {}
		self.calculator = Distance_Calculator("Euclidean")
		self._read_instance()
		self._create_distance_matrix()
		self._extract_name()

	def __call__(self, colony0: Colony, colony1: Colony) -> float:
		return self.distance_matrix[colony0()][colony1()]

	def __getitem__(self, index: int) -> Colony:
		return self.colony_list[self.colony_names[index]]

	def __eq__(self, other: "P2_Instance") -> bool:
		return self.get_name() == other.get_name()

	def get_num_vehicle(self) -> int:
		return self.num_vehicle

	def get_dimension(self) -> int:
		return self.dimension

	def get_num_charging_stations(self) -> int:
		return self.num_charging_stations

	def get_capacity(self) -> int:
		return self.capacity

	def get_battery(self) -> int:
		return self.battery

	def get_energy_factor(self) -> float:
		return self.energy_factor

	def get_optimal_value(self) -> float:
		return self.optimal_value

	def get_central_station(self) -> Colony:
		return self.central_station

	def get_colonies_to_visit(self) -> list[Colony]:
		return self.colonies_to_visit.copy()

	def get_charging_stations(self) -> list[Colony]:
		return self.charging_stations.copy()

	def get_number_of_nodes(self) -> int:
		return self.get_dimension() + self.get_num_charging_stations()

	def get_name(self) -> str:
		return self.name

	def _read_instance(self):
		with open(self.route, "r") as file:
			_, aux = file.readline().strip().split(" ")
			self.optimal_value = float(aux)
			if self.optimal_value == 0:
				self.optimal_value = None
			_, aux = file.readline().strip().split(" ")
			self.num_vehicle = int(aux)
			_, aux = file.readline().strip().split(" ")
			self.dimension = int(aux)
			_, aux = file.readline().strip().split(" ")
			self.num_charging_stations = int(aux)
			_, aux = file.readline().strip().split(" ")
			self.capacity = int(aux)
			_, aux = file.readline().strip().split(" ")
			self.battery = int(aux)
			_, aux = file.readline().strip().split(" ")
			self.energy_factor = float(aux)
			file.readline()
			line = file.readline().strip()
			index = 0
			while line != "SECCION_DEMANDA":
				name, coorx, coory = line.split(" ")
				new_colony = Colony(name, index, tuple([float(coorx), float(coory)]))
				self.colony_list[name] = new_colony
				self.colony_names.append(name)
				self.colonies_to_visit.append(new_colony)
				line = file.readline().strip()
				index += 1
			line = file.readline().strip()
			while line != "ID_NODOS_ESTACIONES_CARGA":
				name, demand = line.split(" ")
				self.colony_list[name].set_demand(int(demand))
				if int(demand) == 0:
					self.central_station = self.colony_list[name]
					self.colonies_to_visit.remove(self.central_station)
					self.charging_stations.append(self.central_station)
				line = file.readline().strip()
			for line in file:
				charge_station = self.colony_list[line.strip()]
				charge_station.set_demand(0)
				self.colonies_to_visit.remove(charge_station)
				self.charging_stations.append(charge_station)

	def _create_distance_matrix(self):
		self.distance_matrix: list[list[float]] = []
		index = 0
		for name_col1 in self.colony_names:
			self.distance_matrix.append([])
			for name_col2 in self.colony_names:
				self.distance_matrix[index].append(self.calculator(self.colony_list[name_col1], self.colony_list[name_col2]))
			index += 1

	def _extract_name(self):
		index = self.route.rfind("/")
		if index == -1:
			index = self.route.rfind("\\")
		self.name = self.route[index + 1:]
