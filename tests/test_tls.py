"""
Unit tests for TLS handshake (stub).
"""
from src.tls.tls_handshake import TLSHandshake
from src.tls.pqc_integration import PQCIntegration

def test_tls_handshake():
    result = TLSHandshake().perform_handshake()
    assert result["signature_valid"]
    assert isinstance(result["shared_secret"], bytes)

def test_pqc_integration():
    pqc = PQCIntegration('ML-KEM')
    assert pqc.integrate()
    pqc = PQCIntegration('ML-DSA')
    assert pqc.integrate()
