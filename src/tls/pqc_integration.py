"""
PQC algorithm integration logic for TLS (demo logic).
"""
from src.crypto.pq_algorithms.ml_kem import MLKEM
from src.crypto.pq_algorithms.ml_dsa import MLDSA

class PQCIntegration:
    def __init__(self, pqc_algorithm='ML-KEM'):
        self.pqc_algorithm = pqc_algorithm

    def integrate(self, data=b"test"):
        if self.pqc_algorithm == 'ML-KEM':
            pub, priv = MLKEM.generate_key_pair()
            ct, ss1 = MLKEM.encapsulate(pub)
            ss2 = MLKEM.decapsulate(ct, priv)
            return ss1 == ss2
        elif self.pqc_algorithm == 'ML-DSA':
            pub, priv = MLDSA.generate_key_pair()
            sig = MLDSA.sign(priv, data)
            return MLDSA.verify(pub, sig, data)
        else:
            return False

if __name__ == "__main__":
    pqc = PQCIntegration('ML-KEM')
    print("PQC KEM integration valid:", pqc.integrate())
    pqc = PQCIntegration('ML-DSA')
    print("PQC DSA integration valid:", pqc.integrate())
