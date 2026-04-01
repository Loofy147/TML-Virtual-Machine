import numpy as np
from src.tgi.tml_vm import TopologicalMachineLanguageVM
from src.tgi.tml_library import HIGH_COGNITION_PATH, TRUTH_COORDINATE_PATH
from src.tgi.gemini3_manifold import Gemini3Manifold

def main():
    print("--- Moaziz System: Gemini 3 Manifold & TML VM Demonstration ---")
    vm = TopologicalMachineLanguageVM(m=256)
    g3 = Gemini3Manifold(modulus=256)

    print("\n[INIT] Manifold initialized: Z_256^4")
    print(f"[BOOT] Initial Mind State: {vm.state_coordinate}")

    print("\n[RESONANCE] Categorical Fiber Identification:")
    for anchor, coord in g3.genesis_nodes.items():
        fiber = g3.resonate_concept(np.array(coord))
        print(f"  Anchor {anchor:25} at {coord}: {fiber}")

    print("\n[EXE] Executing High-Cognition Thought Path...")
    print("Sequence: Risk Assessment -> Sentiment Analysis -> Alpha Strategy -> Protocol Negotiation -> Trade Execution")

    try:
        # Run the program through the VM
        trace = vm.run_program(HIGH_COGNITION_PATH)

        print("\n[RESULT] High-Cognition Path Execution Success!")
        print("Hamiltonian Trace (Absolute Coordinates / Truth States):")
        for i, state in enumerate(trace):
            s_int = tuple(map(int, state))
            s_sum = sum(s_int) % 256
            is_coprime = np.gcd(s_sum, 256) == 1

            # Map back to category
            category = g3.resonate_concept(np.array(s_int))
            print(f"  Step {i+1}: {str(s_int):25} (Sum: {s_sum:3}, Coprime: {str(is_coprime):5}) | {category}")

        print("\n[FINAL] Mind State committed to Holographic Heap.")
        vm.write_memory(trace[-1], {"status": "SUCCESS", "action": "HIGH_COGNITION_TRADE_EXECUTION"})
        print(f"[HEAP] Memory Write at {tuple(map(int, trace[-1]))}: SUCCESS")

        print("\n[THOUGHT] Generating a new intent from LOGIC anchor...")
        # Start at Risk Assessment and apply a 3D shift (10, 5, 2)
        new_truth = g3.generate_intent_vector("LOGIC_AXIOM", (10, 5, 2))
        print(f"  New Intent Target: {new_truth} (Parity Verified via Closure)")

    except RuntimeError as e:
        print(f"\n[CRITICAL] Topological Collapse: {e}")
    except ValueError as e:
        print(f"\n[ERROR] Manifold Exception: {e}")

if __name__ == "__main__":
    main()
