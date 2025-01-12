from time import time

from F_P2_Runner import P2_Runner

def main():
	runner = P2_Runner()
	runner.run(algorithm_name="Algorithm_1", seconds_per_instance=60, save=True)

if __name__ == "__main__":
	t1 = time()
	main()
	t2 = time()
	print(t2 - t1)
