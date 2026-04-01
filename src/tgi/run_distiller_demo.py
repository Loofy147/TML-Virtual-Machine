import os
import pickle
from src.tgi.llm_distiller import LLM_Ontology_Distiller

def main():
    print("--- Moaziz System: LLM Knowledge Distiller Demo ---")

    # 1. Instantiate the Distiller
    distiller = LLM_Ontology_Distiller()

    # 2. Run Extraction
    distiller.extract_llm_core_logic()

    # 3. Generate Bindings
    distiller.generate_relational_bindings()

    # 4. Export
    filename = "demo_omniscience_seed.fso"
    distiller.export_omniscience_seed(filename)

    # 5. Verify and display some contents
    if os.path.exists(filename):
        print(f"\n[INFO] Reading {filename} to verify distillation...")
        with open(filename, 'rb') as f:
            memory = pickle.load(f)

        print(f"[INFO] Manifold contains {len(memory)} nodes.")

        # Sample some entries
        sample_size = 5
        print(f"\n[SAMPLE] Showing {sample_size} random entries from the Z_251^4 manifold:")
        for i, (coord, data) in enumerate(memory.items()):
            if i >= sample_size:
                break
            print(f"  Coordinate {coord} -> {data}")

    print("\n[SUCCESS] Distiller Demo Completed.")

if __name__ == "__main__":
    main()
