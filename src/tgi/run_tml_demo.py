import numpy as np
from src.tgi.tml_vm import TopologicalMachineLanguageVM
from src.tgi.tml_library import MASSIVE_AGENT_ACTION

def main():
    print("--- Moaziz System: TML Virtual Machine Execution ---")
    vm = TopologicalMachineLanguageVM(m=256)

    print("\n[INIT] Manifold initialized: Z_256^4")
    print(f"[BOOT] Initial Mind State: {vm.state_coordinate}")

    print("\n[EXE] Executing Massive Agent Action...")
    print("Sequence: Bootstrap -> API Standardization -> Crypto Verification -> Trade Routing")

    try:
        trace = vm.run_program(MASSIVE_AGENT_ACTION)

        print("\n[RESULT] Execution Success!")
        print("Hamiltonian Trace (4D State Map):")
        for i, state in enumerate(trace):
            s_int = tuple(map(int, state))
            s_sum = sum(s_int) % 256
            print(f"  Step {i+1}: {s_int} (Manifold Sum: {s_sum}, Coprime: {np.gcd(s_sum, 256)==1})")

        print("\n[FINAL] Mind State committed to Holographic Heap.")
        vm.write_memory(trace[-1], {"status": "SUCCESS", "action": "MASSIVE_AGENT_ACTION"})
        print(f"[HEAP] Memory Write at {tuple(map(int, trace[-1]))}: SUCCESS")

    except RuntimeError as e:
        print(f"\n[CRITICAL] Topological Collapse: {e}")
    except ValueError as e:
        print(f"\n[ERROR] Memory Exception: {e}")

if __name__ == "__main__":
    main()
