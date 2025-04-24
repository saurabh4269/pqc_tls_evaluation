#!/bin/bash
# Script to run TLS handshake experiments and collect timing results
set -e

ALG=$1
if [ -z "$ALG" ]; then
  echo "Usage: $0 <algorithm>"
  exit 1
fi

RESULTS_DIR="../results"
TIME_CSV="$RESULTS_DIR/time_results.csv"

# Run handshake and measure time using Python
TIME=$(python3 -c "import time; from src.tls.tls_handshake import TLSHandshake; start=time.time(); TLSHandshake(use_hybrid=True).perform_handshake(); print(f'{time.time()-start:.6f}')")

# Append result to CSV
if [ ! -f "$TIME_CSV" ]; then
  echo "algorithm,time" > "$TIME_CSV"
fi
echo "$ALG,$TIME" >> "$TIME_CSV"

echo "Experiment for $ALG completed. Time: $TIME seconds."
