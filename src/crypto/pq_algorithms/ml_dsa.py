"""
ML-DSA (Dilithium) implementation using python-oqs.
"""
import oqs

class MLDSA:
    @staticmethod
    def generate_key_pair():
        with oqs.Signature('Dilithium5') as sig:
            public_key = sig.generate_keypair()
            private_key = sig.export_secret_key()
            return public_key, private_key

    @staticmethod
    def sign(private_key, data: bytes) -> bytes:
        with oqs.Signature('Dilithium5') as sig:
            sig.import_secret_key(private_key)
            return sig.sign(data)

    @staticmethod
    def verify(public_key, signature: bytes, data: bytes) -> bool:
        with oqs.Signature('Dilithium5') as sig:
            sig.import_public_key(public_key)
            return sig.verify(data, signature)

if __name__ == "__main__":
    pub, priv = MLDSA.generate_key_pair()
    msg = b"test"
    sig = MLDSA.sign(priv, msg)
    print("Signature valid:", MLDSA.verify(pub, sig, msg))
