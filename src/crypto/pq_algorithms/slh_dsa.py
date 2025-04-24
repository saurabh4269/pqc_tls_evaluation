"""
SLH-DSA (Falcon) implementation using python-oqs.
"""
import oqs

class SLHDSA:
    @staticmethod
    def generate_key_pair():
        with oqs.Signature('Falcon-1024') as sig:
            public_key = sig.generate_keypair()
            private_key = sig.export_secret_key()
            return public_key, private_key

    @staticmethod
    def sign(private_key, data: bytes) -> bytes:
        with oqs.Signature('Falcon-1024') as sig:
            sig.import_secret_key(private_key)
            return sig.sign(data)

    @staticmethod
    def verify(public_key, signature: bytes, data: bytes) -> bool:
        with oqs.Signature('Falcon-1024') as sig:
            sig.import_public_key(public_key)
            return sig.verify(data, signature)

if __name__ == "__main__":
    pub, priv = SLHDSA.generate_key_pair()
    msg = b"test"
    sig = SLHDSA.sign(priv, msg)
    print("Signature valid:", SLHDSA.verify(pub, sig, msg))
