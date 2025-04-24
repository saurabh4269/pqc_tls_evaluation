"""
Hybrid Signatures: Combines ECDSA and Dilithium for hybrid authentication using real signatures.
"""
from src.crypto.traditional_algorithms.ecdh import ECDH
from src.crypto.pq_algorithms.ml_dsa import MLDSA
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature, decode_dss_signature

class HybridSignatures:
    @staticmethod
    def generate_key_pair():
        ecdsa_priv = ECDH.generate_key_pair()
        mldsa_pub, mldsa_priv = MLDSA.generate_key_pair()
        return (ecdsa_priv, mldsa_pub, mldsa_priv)

    @staticmethod
    def sign(ecdsa_priv, mldsa_priv, data: bytes):
        ecdsa_sig = ecdsa_priv.sign(data, ec.ECDSA(hashes.SHA256()))
        mldsa_sig = MLDSA.sign(mldsa_priv, data)
        return ecdsa_sig + mldsa_sig

    @staticmethod
    def verify(ecdsa_pub, mldsa_pub, signature: bytes, data: bytes):
        # Split signature: ECDSA is variable length, so this is a demo split
        ecdsa_sig = signature[:72]  # ECDSA signature length can vary
        mldsa_sig = signature[72:]
        try:
            ecdsa_pub.verify(ecdsa_sig, data, ec.ECDSA(hashes.SHA256()))
            mldsa_valid = MLDSA.verify(mldsa_pub, mldsa_sig, data)
            return mldsa_valid
        except Exception:
            return False

if __name__ == "__main__":
    ecdsa_priv, mldsa_pub, mldsa_priv = HybridSignatures.generate_key_pair()
    ecdsa_pub = ecdsa_priv.public_key()
    msg = b"test"
    sig = HybridSignatures.sign(ecdsa_priv, mldsa_priv, msg)
    print("Hybrid signature valid:", HybridSignatures.verify(ecdsa_pub, mldsa_pub, sig, msg))
