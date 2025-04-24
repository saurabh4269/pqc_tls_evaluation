#!/bin/bash
# Script to generate traditional, PQC, and hybrid certificates
set -e

CERT_DIR="../data/certificates"
KEY_DIR="../data/keys"
mkdir -p "$CERT_DIR" "$KEY_DIR"

# Traditional (ECDSA)
echo "Generating traditional ECDSA certificate..."
openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:prime256v1 -keyout "$KEY_DIR/traditional_key.pem" -out "$CERT_DIR/traditional_cert.pem" -days 365 -nodes -subj "/CN=Traditional"

# PQC (Dilithium) - requires OQS-OpenSSL
echo "Generating PQC (Dilithium) certificate..."
if openssl version | grep -q 'OQS'; then
  openssl req -x509 -newkey dilithium3 -keyout "$KEY_DIR/pq_key.pem" -out "$CERT_DIR/pq_cert.pem" -days 365 -nodes -subj "/CN=PQC-Dilithium"
else
  echo "OQS-OpenSSL not found. Please install OQS-OpenSSL for PQC certs. Creating placeholder."
  touch "$KEY_DIR/pq_key.pem" "$CERT_DIR/pq_cert.pem"
fi

# Hybrid (ECDSA+Dilithium) - requires OQS-OpenSSL
echo "Generating hybrid (ECDSA+Dilithium) certificate..."
if openssl version | grep -q 'OQS'; then
  openssl req -x509 -newkey ecdsa_dilithium3 -keyout "$KEY_DIR/hybrid_key.pem" -out "$CERT_DIR/hybrid_cert.pem" -days 365 -nodes -subj "/CN=Hybrid-ECDSA-Dilithium"
else
  echo "OQS-OpenSSL not found. Please install OQS-OpenSSL for hybrid certs. Creating placeholder."
  touch "$KEY_DIR/hybrid_key.pem" "$CERT_DIR/hybrid_cert.pem"
fi

echo "Certificates generated in $CERT_DIR and $KEY_DIR."
