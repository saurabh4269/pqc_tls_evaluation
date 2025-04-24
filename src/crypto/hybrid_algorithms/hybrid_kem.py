"""
Hybrid KEM: Combines ECDH and ML-KEM for hybrid key exchange using real secrets.
"""
from src.crypto.traditional_algorithms.ecdh import ECDH
from src.crypto.pq_algorithms.ml_kem import MLKEM
from cryptography.hazmat.primitives.kdf.concatkdf import ConcatKDFHash
from cryptography.hazmat.primitives import hashes

class HybridKEM:
    @staticmethod
    def generate_key_pair():
        ecdh_priv = ECDH.generate_key_pair()
        mlkem_pub, mlkem_priv = MLKEM.generate_key_pair()
        return (ecdh_priv, mlkem_pub, mlkem_priv)

    @staticmethod
    def encapsulate(ecdh_pub, mlkem_pub):
        # ECDH shared secret
        # For demo, generate a new ECDH key for the peer
        peer_priv = ECDH.generate_key_pair()
        ecdh_secret = ECDH.derive_shared_secret(peer_priv, ecdh_pub)
        mlkem_ct, mlkem_secret = MLKEM.encapsulate(mlkem_pub)
        # Combine secrets using a KDF
        kdf = ConcatKDFHash(algorithm=hashes.SHA256(), length=32, otherinfo=None)
        hybrid_secret = kdf.derive(ecdh_secret + mlkem_secret)
        return (mlkem_ct, hybrid_secret)

    @staticmethod
    def decapsulate(ecdh_priv, mlkem_ct, mlkem_priv, peer_pub):
        ecdh_secret = ECDH.derive_shared_secret(ecdh_priv, peer_pub)
        mlkem_secret = MLKEM.decapsulate(mlkem_ct, mlkem_priv)
        kdf = ConcatKDFHash(algorithm=hashes.SHA256(), length=32, otherinfo=None)
        hybrid_secret = kdf.derive(ecdh_secret + mlkem_secret)
        return hybrid_secret

if __name__ == "__main__":
    ecdh_priv = ECDH.generate_key_pair()
    ecdh_pub = ecdh_priv.public_key()
    mlkem_pub, mlkem_priv = MLKEM.generate_key_pair()
    mlkem_ct, shared1 = HybridKEM.encapsulate(ecdh_pub, mlkem_pub)
    shared2 = HybridKEM.decapsulate(ecdh_priv, mlkem_ct, mlkem_priv, ecdh_pub)
    print("Hybrid shared secrets match:", shared1 == shared2)
