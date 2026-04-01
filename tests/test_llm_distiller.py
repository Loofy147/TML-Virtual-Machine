import unittest
import os
import pickle
import numpy as np
from src.tgi.llm_distiller import HolographicFSO_Engine, LLM_Ontology_Distiller
from math import gcd

class TestLLMDistiller(unittest.TestCase):
    def setUp(self):
        self.engine = HolographicFSO_Engine(m=251, dim=1024)
        self.distiller = LLM_Ontology_Distiller()

    def test_basis_vector_determinism(self):
        v1 = self.engine.generate_basis_vector("test")
        v2 = self.engine.generate_basis_vector("test")
        np.testing.assert_array_equal(v1, v2)

    def test_bind_shape(self):
        v1 = self.engine.generate_basis_vector("v1")
        v2 = self.engine.generate_basis_vector("v2")
        bound = self.engine.bind(v1, v2)
        self.assertEqual(bound.shape, (1024,))
        self.assertTrue(np.all(bound >= 0) and np.all(bound < 251))

    def test_collapse_parity(self):
        v = self.engine.generate_basis_vector("test_collapse")
        coord = self.engine.collapse_to_torus(v)
        self.assertEqual(len(coord), 4)
        self.assertEqual(gcd(sum(coord), 251), 1)

    def test_distillation_process(self):
        test_seed = "test_omniscience_seed.fso"
        if os.path.exists(test_seed):
            os.remove(test_seed)

        self.distiller.extract_llm_core_logic()
        self.distiller.generate_relational_bindings()
        self.distiller.export_omniscience_seed(test_seed)

        self.assertTrue(os.path.exists(test_seed))

        with open(test_seed, 'rb') as f:
            data = pickle.load(f)

        self.assertGreater(len(data), 0)
        types = {item['type'] for item in data.values()}
        self.assertIn('grammar', types)

        os.remove(test_seed)

    def test_import_and_expansion(self):
        seed1 = "seed1.fso"
        seed2 = "seed2.fso"

        # 1. Create first seed with one entry
        dist1 = LLM_Ontology_Distiller()
        v = dist1.engine.generate_basis_vector("entry1")
        c = dist1.engine.collapse_to_torus(v)
        dist1.global_seed_memory[c] = {"type": "test", "val": 1}
        dist1.export_omniscience_seed(seed1)

        # 2. Create second distiller, import seed1, add another entry
        dist2 = LLM_Ontology_Distiller()
        dist2.import_omniscience_seed(seed1)
        self.assertIn(c, dist2.global_seed_memory)

        v2 = dist2.engine.generate_basis_vector("entry2")
        c2 = dist2.engine.collapse_to_torus(v2)
        dist2.global_seed_memory[c2] = {"type": "test", "val": 2}
        dist2.export_omniscience_seed(seed2)

        # 3. Verify seed2 has both entries
        with open(seed2, 'rb') as f:
            data = pickle.load(f)
        self.assertIn(c, data)
        self.assertIn(c2, data)
        self.assertEqual(len(data), 2)

        # Cleanup
        if os.path.exists(seed1): os.remove(seed1)
        if os.path.exists(seed2): os.remove(seed2)

if __name__ == '__main__':
    unittest.main()
