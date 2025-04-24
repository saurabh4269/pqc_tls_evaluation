"""
Hybrid KEM: Combines ECDH and ML-KEM for hybrid key exchange.
Expanded: Add docstring and usage example for HybridKEM.
"""
from src.crypto.traditional_algorithms.ecdh import ECDH
from src.crypto.pq_algorithms.ml_kem import MLKEM

class HybridKEM:
    @staticmethod
    def generate_key_pair():
        ecdh_priv = ECDH.generate_key_pair()
        mlkem_pub, mlkem_priv = MLKEM.generate_key_pair()
        return (ecdh_priv, mlkem_pub, mlkem_priv)

    @staticmethod
    def encapsulate(ecdh_pub, mlkem_pub):
        # ECDH shared secret
        # ML-KEM shared secret
        ecdh_secret = b"ecdh_shared_secret"  # Placeholder
        mlkem_ct, mlkem_secret = MLKEM.encapsulate(mlkem_pub)
        # Combine secrets (e.g., concatenate or KDF)
        return (mlkem_ct, ecdh_secret + mlkem_secret)

    @staticmethod
    def decapsulate(ecdh_priv, mlkem_ct, mlkem_priv):
        # ECDH shared secret
        # ML-KEM shared secret
        ecdh_secret = b"ecdh_shared_secret"  # Placeholder
        mlkem_secret = MLKEM.decapsulate(mlkem_ct, mlkem_priv)
        return ecdh_secret + mlkem_secret

if __name__ == "__main__":
    # Example usage (stub)
    ecdh_priv, mlkem_pub, mlkem_priv = HybridKEM.generate_key_pair()
    mlkem_ct, shared1 = HybridKEM.encapsulate(None, mlkem_pub)
    shared2 = HybridKEM.decapsulate(ecdh_priv, mlkem_ct, mlkem_priv)
    print("Hybrid shared secrets match (stub):", shared1 == shared2)
