"""
RSA key generation, signing, and verification using cryptography.

Expanded: Example usage and docstrings for RSA crypto module.
"""
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

class RSA:
    """
    RSA key generation, signing, and verification.
    """
    @staticmethod
    def generate_key_pair(key_size=2048):
        """
        Generate an RSA key pair.

        :param key_size: Size of the key, default is 2048 bits.
        :return: RSA private key.
        """
        return rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )

    @staticmethod
    def sign(private_key, data: bytes) -> bytes:
        """
        Sign data using RSA private key.

        :param private_key: RSA private key.
        :param data: Data to be signed.
        :return: Signature.
        """
        return private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    @staticmethod
    def verify(public_key, signature: bytes, data: bytes) -> bool:
        """
        Verify RSA signature.

        :param public_key: RSA public key.
        :param signature: Signature to be verified.
        :param data: Data that was signed.
        :return: True if signature is valid, False otherwise.
        """
        try:
            public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False

if __name__ == "__main__":
    # Example usage
    priv = RSA.generate_key_pair()
    pub = priv.public_key()
    msg = b"test message"
    sig = RSA.sign(priv, msg)
    print("Signature valid:", RSA.verify(pub, sig, msg))
