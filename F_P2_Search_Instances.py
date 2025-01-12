import os

from F_P2_Instance import P2_Instance

class P2_Search_Instances():
	def __init__(self):
		self.instances_list: list[P2_Instance] = []
		self.total_unit = 0
		self._search_instances_directory()
		self._list_instances()

	def __iter__(self):
		return iter(self.instances_list)

	def __call__(self, n_instance: int) -> P2_Instance:
		if type(n_instance) is not int:
			raise TypeError("El parametro dado debe ser un entero.")
		if n_instance >= len(self.instances_list):
			raise ValueError("El valor dado debe ser menor al numero de instancias.")
		return self.instances_list[n_instance]

	def _search_instances_directory(self):
		file_path = os.path.abspath(os.path.dirname(__file__))
		for actual_dir, sub_dir, _ in os.walk(file_path):
			if 'Instances' in sub_dir:
				self.path_instances = os.path.join(actual_dir, 'Instances')
				return
			if 'instances' in sub_dir:
				self.path_instances = os.path.join(actual_dir, 'instances')
				return
		raise ValueError("No existe carpeta Instances en el directorio raiz.")

	def _list_instances(self):
		for path, _, files in os.walk(self.path_instances):
			for file in files:
				if file.startswith("instancia") and file.endswith(".txt"):
					inst = P2_Instance(os.path.join(path, file))
					self.instances_list.append(inst)
					self.total_unit += inst.get_number_of_nodes()
		if not self.instances_list:
			raise ValueError("No existen instancias en la carpeta de instancias.")
