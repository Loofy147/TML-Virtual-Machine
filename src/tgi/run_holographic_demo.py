import numpy as np
from src.tgi.holographic_fso import HolographicFSO_Engine
from src.tgi.tml_vm import TopologicalMachineLanguageVM

def main():
    print("--- Moaziz System: Holographic FSO Demonstration ---")
    fso = HolographicFSO_Engine(m=251, dim=1024)
    vm = TopologicalMachineLanguageVM(m=251) # Use same modulus as FSO

    print("\n[STEP 1] Generating High-Dimensional Basis Vectors...")
    v_logic = fso.generate_basis_vector("SYSTEM_PROMPT_AXIOMS")
    v_finance = fso.generate_basis_vector("XAUUSD_GARCH_MODELS")
    v_action = fso.generate_basis_vector("EXECUTE_TRADE_STRATEGY")
    print(f"  Logic Dimension: {v_logic.shape}")
    print(f"  Finance Dimension: {v_finance.shape}")
    print(f"  Action Dimension: {v_action.shape}")

    print("\n[STEP 2] Executing Holographic Binding (FSO Folding)...")
    # Bind Logic to Finance -> Create Strategy Relationship
    v_strategy = fso.bind(v_logic, v_finance)
    # Bind Strategy to Action -> Complete Intelligence Sequence
    v_full_intent = fso.bind(v_strategy, v_action)

    print("  Updating Global Memory Trace with Intent...")
    fso.update_trace(v_full_intent)

    print("\n[STEP 3] Verifying Mathematical Recovery (Un-binding)...")
    # To recover v_action from v_full_intent, we unbind with v_strategy
    v_recovered_action = fso.unbind(v_full_intent, v_strategy)

    # Calculate recovery accuracy (Similarity)
    similarity = np.dot(v_recovered_action, v_action) / (np.linalg.norm(v_recovered_action) * np.linalg.norm(v_action))
    print(f"  Action Recovery Similarity: {similarity:.4f}")

    if similarity > 0.8:
        print("  [SUCCESS] Intelligence Sequence is mathematically sound.")
    else:
        print("  [WARNING] High-Dimensional Drift detected.")

    print("\n[STEP 4] Collapsing Latent Space to 4D Torus...")
    execution_coordinate = fso.collapse_to_torus(fso.memory_trace)
    print(f"  Final Execution Coordinate (Z_251^4): {execution_coordinate}")

    print("\n[STEP 5] Deploying Coordinate to TML VM Execution Layer...")
    try:
        # Move state to the holographic result
        # Note: execute_vector is relative, so we move from current (0,0,0,0)
        final_state = vm.execute_vector(execution_coordinate)
        print(f"  VM Mind State Committed: {final_state}")
        print("  [PARITY] H2 Harmony Verified.")
    except RuntimeError as e:
        print(f"  [CRITICAL] Topological Exception: {e}")

if __name__ == "__main__":
    main()
