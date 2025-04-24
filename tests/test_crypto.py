"""
Tests for crypto algorithms (stub).
"""
from src.crypto.traditional_algorithms.rsa import RSA
from src.crypto.traditional_algorithms.ecdh import ECDH
from src.crypto.pq_algorithms.ml_kem import MLKEM
from src.crypto.pq_algorithms.ml_dsa import MLDSA
from src.crypto.pq_algorithms.slh_dsa import SLHDSA
from src.crypto.hybrid_algorithms.hybrid_kem import HybridKEM
from src.crypto.hybrid_algorithms.hybrid_signatures import HybridSignatures

def test_rsa():
    priv = RSA.generate_key_pair()
    pub = priv.public_key()
    msg = b"test"
    sig = RSA.sign(priv, msg)
    assert RSA.verify(pub, sig, msg)

def test_ecdh():
    priv1 = ECDH.generate_key_pair()
    priv2 = ECDH.generate_key_pair()
    pub2 = priv2.public_key()
    shared1 = ECDH.derive_shared_secret(priv1, pub2)
    pub1 = priv1.public_key()
    shared2 = ECDH.derive_shared_secret(priv2, pub1)
    assert shared1 == shared2

def test_mlkem():
    pub, priv = MLKEM.generate_key_pair()
    ct, ss1 = MLKEM.encapsulate(pub)
    ss2 = MLKEM.decapsulate(ct, priv)
    assert ss1 == ss2

def test_mldsa():
    pub, priv = MLDSA.generate_key_pair()
    msg = b"test"
    sig = MLDSA.sign(priv, msg)
    assert MLDSA.verify(pub, sig, msg)

def test_slhdsa():
    pub, priv = SLHDSA.generate_key_pair()
    msg = b"test"
    sig = SLHDSA.sign(priv, msg)
    assert SLHDSA.verify(pub, sig, msg)

def test_hybrid_kem():
    ecdh_priv = ECDH.generate_key_pair()
    ecdh_pub = ecdh_priv.public_key()
    mlkem_pub, mlkem_priv = MLKEM.generate_key_pair()
    mlkem_ct, shared1 = HybridKEM.encapsulate(ecdh_pub, mlkem_pub)
    shared2 = HybridKEM.decapsulate(ecdh_priv, mlkem_ct, mlkem_priv, ecdh_pub)
    assert shared1 == shared2

def test_hybrid_signatures():
    ecdsa_priv, mldsa_pub, mldsa_priv = HybridSignatures.generate_key_pair()
    ecdsa_pub = ecdsa_priv.public_key()
    msg = b"test"
    sig = HybridSignatures.sign(ecdsa_priv, mldsa_priv, msg)
    assert HybridSignatures.verify(ecdsa_pub, mldsa_pub, sig, msg)
