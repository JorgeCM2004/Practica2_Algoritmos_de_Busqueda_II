import sys
import os
from time import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Tests.F_P2_Tests import P2_Tests

def test_algorithm1():
	tester = P2_Tests()
	init_time = time()
	tester.run_test("Algorithm_1")
	final_time = time()
	assert final_time - init_time <= 60 * max(tester.get_number_of_tests(), tester.get_number_of_instances())

def test_algorithm2():
	tester = P2_Tests()
	init_time = time()
	tester.run_test("Algorithm_2")
	final_time = time()
	assert final_time - init_time <= 60 * max(tester.get_number_of_tests(), tester.get_number_of_instances())
