import unittest
import numpy as np
from src.tgi.tml_vm import TopologicalMachineLanguageVM

class TestTMLVM(unittest.TestCase):
    def setUp(self):
        self.vm = TopologicalMachineLanguageVM(m=256)

    def test_parity_harmony(self):
        # Sum is 1, which is coprime to 256
        self.assertTrue(self.vm._check_parity_harmony(np.array([0, 0, 0, 1])))
        # Sum is 2, not coprime to 256
        self.assertFalse(self.vm._check_parity_harmony(np.array([0, 0, 0, 2])))

    def test_force_closure(self):
        w = self.vm.force_closure(1, 2, 3)
        self.assertTrue(self.vm._check_parity_harmony(np.array([1, 2, 3, w])))

    def test_execute_vector(self):
        # 15+30+45+121 = 211 (coprime)
        # Vector 1: (0,0,0,0) + (15, 30, 45, 121) = (15, 30, 45, 121) -> Sum 211 (coprime)
        vector = (15, 30, 45, 121)
        new_state = self.vm.execute_vector(vector)
        self.assertEqual(tuple(map(int, new_state)), vector)

        # Test valid move from (15, 30, 45, 121)
        # We need sum(new_state) to be coprime to 256.
        # Current sum = 211. 211 + 2 = 213 (coprime to 256)
        valid_vector = (0, 0, 0, 2)
        state = self.vm.execute_vector(valid_vector)
        self.assertEqual(tuple(map(int, state)), (15, 30, 45, 123))

        # Test invalid move
        # 213 + 1 = 214 (not coprime)
        invalid_vector = (0, 0, 0, 1)
        with self.assertRaises(RuntimeError):
            self.vm.execute_vector(invalid_vector)

    def test_write_memory(self):
        valid_coord = (0, 0, 0, 1)
        self.vm.write_memory(valid_coord, "test_data")
        self.assertEqual(self.vm.holographic_heap[valid_coord], "test_data")

        invalid_coord = (0, 0, 0, 2)
        with self.assertRaises(ValueError):
            self.vm.write_memory(invalid_coord, "bad_data")

    def test_run_program(self):
        # Program designed to always land on coprime sums
        # Start: (0,0,0,0) Sum 0
        # 1. (0,0,0,1) -> (0,0,0,1) Sum 1. OK.
        # 2. (0,0,0,2) -> (0,0,0,3) Sum 3. OK.
        # 3. (0,0,0,2) -> (0,0,0,5) Sum 5. OK.
        valid_program = [
            (0, 0, 0, 1),
            (0, 0, 0, 2),
            (0, 0, 0, 2),
        ]
        trace = self.vm.run_program(valid_program)
        self.assertEqual(len(trace), 3)
        self.assertEqual(tuple(map(int, trace[0])), (0, 0, 0, 1))
        self.assertEqual(tuple(map(int, trace[1])), (0, 0, 0, 3))
        self.assertEqual(tuple(map(int, trace[2])), (0, 0, 0, 5))

if __name__ == '__main__':
    unittest.main()
