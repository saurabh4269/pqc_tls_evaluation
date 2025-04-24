"""
Hybrid key exchange orchestration (high-level stub).

Expanded: Add docstring and usage example for HybridKeyExchange.
"""
class HybridKeyExchange:
    def __init__(self, traditional_alg, pqc_alg):
        self.traditional_alg = traditional_alg
        self.pqc_alg = pqc_alg

    def perform(self):
        # Orchestrate hybrid key exchange
        return f"Hybrid key exchange: {self.traditional_alg} + {self.pqc_alg}"

if __name__ == "__main__":
    # Example usage (stub)
    hke = HybridKeyExchange("ECDH", "ML-KEM")
    print(hke.perform())
