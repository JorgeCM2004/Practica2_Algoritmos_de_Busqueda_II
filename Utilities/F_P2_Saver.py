import os

from Interfaces.F_Solution_Route import Solution_Route

ABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CSV_HEADER = "Instance_Name, Value, Solution, CPU_Time\n"
DELIMITER = ", "

class P2_Saver():
	def save(self, solution_list: list[Solution_Route]):
		dicted = {}
		try:
			with open(os.path.join(ABS_PATH, "Saves\\Best_Save.csv"), "r") as file:
				file.readline()
				for line in file:
					line = line.strip().split(DELIMITER)
					line = [line[0], line[1], ", ".join(line[2 : -1]), line[-1]]
					dicted[line[0]] = (line[1], line[2], line[3])
		except:
			pass
		with open(os.path.join(ABS_PATH, "Saves\\Last_Save.csv"), "w") as file:
			file.write(CSV_HEADER)
			for solution in solution_list:
				line = ""
				line = solution.get_instance().get_name() + DELIMITER
				line += str(solution.get_of_value()) + DELIMITER
				line += str(solution) + DELIMITER
				line += str(solution.get_CPU_time()) + "\n"
				file.write(line)
		with open(os.path.join(ABS_PATH, "Saves\\Best_Save.csv"), "w") as file:
			file.write(CSV_HEADER)
			for solution in solution_list:
				if solution.get_instance().get_name() in dicted:
					if solution.get_of_value() < float(dicted[solution.get_instance().get_name()][0]):
						line = ""
						line = solution.get_instance().get_name() + DELIMITER
						line += str(solution.get_of_value()) + DELIMITER
						line += str(solution) + DELIMITER
						line += str(solution.get_CPU_time()) + "\n"
						file.write(line)
					else:
						line = ""
						line = solution.get_instance().get_name() + DELIMITER
						line += dicted[solution.get_instance().get_name()][0] + DELIMITER
						line += dicted[solution.get_instance().get_name()][1] + DELIMITER
						line += dicted[solution.get_instance().get_name()][2] + "\n"
						file.write(line)
				else:
					line = ""
					line = solution.get_instance().get_name() + DELIMITER
					line += str(solution.get_of_value()) + DELIMITER
					line += str(solution) + DELIMITER
					line += str(solution.get_CPU_time()) + "\n"
					file.write(line)
