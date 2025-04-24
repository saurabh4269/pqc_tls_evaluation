"""
ECDH key exchange using cryptography.

Expanded: Example usage and docstrings for ECDH crypto module.
"""
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class ECDH:
    @staticmethod
    def generate_key_pair():
        """
        Generate a private key for ECDH key exchange.
        """
        return ec.generate_private_key(ec.SECP256R1(), default_backend())

    @staticmethod
    def derive_shared_secret(private_key, peer_public_key):
        """
        Derive a shared secret using a private key and a peer's public key.
        """
        return private_key.exchange(ec.ECDH(), peer_public_key)

if __name__ == "__main__":
    # Example usage
    priv1 = ECDH.generate_key_pair()
    priv2 = ECDH.generate_key_pair()
    pub2 = priv2.public_key()
    shared1 = ECDH.derive_shared_secret(priv1, pub2)
    pub1 = priv1.public_key()
    shared2 = ECDH.derive_shared_secret(priv2, pub1)
    print("Shared secrets match:", shared1 == shared2)
