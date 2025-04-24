#!/bin/bash
# Script to run TLS handshake experiments
set -e

ALG=$1
if [ -z "$ALG" ]; then
  echo "Usage: $0 <algorithm>"
  exit 1
fi

echo "Running TLS handshake experiment for $ALG..."
# Placeholder: Replace with actual TLS handshake command using OQS-OpenSSL
# Example: openssl s_client -connect localhost:4433 -groups $ALG

echo "Experiment for $ALG completed."
