"""
ML-KEM (Kyber) implementation using python-oqs.
"""
import oqs

class MLKEM:
    @staticmethod
    def generate_key_pair():
        with oqs.KeyEncapsulation('Kyber1024') as kem:
            public_key = kem.generate_keypair()
            private_key = kem.export_secret_key()
            return public_key, private_key

    @staticmethod
    def encapsulate(public_key):
        with oqs.KeyEncapsulation('Kyber1024') as kem:
            kem.import_public_key(public_key)
            ciphertext, shared_secret = kem.encap_secret()
            return ciphertext, shared_secret

    @staticmethod
    def decapsulate(ciphertext, private_key):
        with oqs.KeyEncapsulation('Kyber1024') as kem:
            kem.import_secret_key(private_key)
            shared_secret = kem.decap_secret(ciphertext)
            return shared_secret

if __name__ == "__main__":
    pub, priv = MLKEM.generate_key_pair()
    ct, ss1 = MLKEM.encapsulate(pub)
    ss2 = MLKEM.decapsulate(ct, priv)
    print("Shared secrets match:", ss1 == ss2)
