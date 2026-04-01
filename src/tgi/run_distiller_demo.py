import os
import pickle
from src.tgi.llm_distiller import LLM_Ontology_Distiller

def main():
    print("--- Moaziz System: LLM Knowledge Distiller Demo ---")

    filename = "demo_omniscience_seed.fso"
    if os.path.exists(filename):
        os.remove(filename)

    # 1. First Pass: Extract Core Logic
    print("\n[PHASE 1] Initial Distillation...")
    distiller = LLM_Ontology_Distiller()
    distiller.extract_llm_core_logic()
    distiller.export_omniscience_seed(filename)

    # 2. Second Pass: Load, Expand with Relational Bindings
    print("\n[PHASE 2] Loading and Expanding Manifold...")
    expander = LLM_Ontology_Distiller()
    if expander.import_omniscience_seed(filename):
        print("  [SUCCESS] Existing manifold loaded.")

    expander.generate_relational_bindings()

    # Add custom knowledge node
    v_custom = expander.engine.generate_basis_vector("CUSTOM_PROTOCOL_X")
    c_custom = expander.engine.collapse_to_torus(v_custom)
    expander.global_seed_memory[c_custom] = {"type": "custom", "name": "PROTOCOL_X"}

    # Export expanded manifold
    expander.export_omniscience_seed(filename)

    # 3. Final Verification
    if os.path.exists(filename):
        print(f"\n[PHASE 3] Final Verification of {filename}...")
        with open(filename, 'rb') as f:
            memory = pickle.load(f)

        print(f"[INFO] Expanded manifold contains {len(memory)} nodes.")

        # Check for both core and expanded knowledge
        types = {item['type'] for item in memory.values()}
        print(f"[INFO] Node types present: {types}")

        if 'grammar' in types and 'relation' in types and 'custom' in types:
            print("  [SUCCESS] All phases of knowledge integration verified.")

    print("\n[SUCCESS] Distiller Demo Completed.")

if __name__ == "__main__":
    main()
