# Post-Quantum Cryptography Evaluation in TLS 1.3  
**Evaluating PQC Key Exchange and Authentication Algorithms**  

## Table of Contents  
1. [Overview](#overview)  
2. [Features](#features)  
3. [Project Structure](#project-structure)  
4. [Prerequisites](#prerequisites)  
5. [Installation](#installation)  
6. [Usage](#usage)  
   - [Generate Certificates](#generate-certificates)  
   - [Run TLS Experiments](#run-tls-experiments)  
   - [Performance Evaluation](#performance-evaluation)  
7. [Performance Metrics](#performance-metrics)  
8. [References](#references)  

---

## Project Progress (as of April 2025)
- The codebase is fully scaffolded with all modules, scripts, and test stubs as described in the project structure.
- All crypto, hybrid, PQC, TLS, performance, and utility modules include docstrings and example usage for clarity and ease of extension.
- CSV result files for time, energy, and memory metrics are initialized with headers.
- An MIT LICENSE file is included.
- The code is ready for real PQC integration (e.g., with python-oqs) and further development or automation.
- See each module for usage examples and further documentation.

---

## What’s Next / To-Do
- [ ] **Integrate Real PQC Algorithms:**
  - Replace stubs in `ml_kem.py`, `ml_dsa.py`, and `slh_dsa.py` with real implementations using `python-oqs` or similar.
  - Update hybrid modules to use real shared secrets and signatures.
- [ ] **Expand TLS Logic:**
  - Implement actual TLS handshake flows using Python libraries or by wrapping OpenSSL/OQS-OpenSSL commands.
  - Add certificate validation and mutual authentication.
- [ ] **Automate Experiments:**
  - Enhance scripts to run full handshake and performance experiments, collect results, and append to CSVs.
- [ ] **Improve Testing:**
  - Add real test cases for each crypto and performance module.
  - Use pytest for more comprehensive testing and reporting.
- [ ] **Documentation:**
  - Expand the README with usage examples, architecture diagrams, and troubleshooting tips.
- [ ] **Advanced Features:**
  - Add bandwidth measurement automation.
  - Add support for additional PQC algorithms as they become available.

---

## **Overview**  
This project evaluates the performance of **Post-Quantum Cryptography (PQC)** algorithms in **TLS 1.3**, focusing on key exchange (e.g., ML-KEM) and authentication (e.g., ML-DSA/SLH-DSA) mechanisms. The goal is to measure computational efficiency (time, energy, memory) and compare hybrid (traditional + PQC) and pure PQC algorithms against classical cryptographic primitives (ECDH, RSA).  

The work aligns with the IETF draft [draft-reddy-uta-pqc-app](https://datatracker.ietf.org/doc/draft-reddy-uta-pqc-app/), which provides guidelines for integrating PQC into TLS-based applications.  

---

## **Features**  
- **Hybrid Key Exchange**:  
  - Combine traditional (X25519, SecP256r1) and PQC algorithms (ML-KEM-768).  
  - Example: `X25519MLKEM768`, `SecP256r1MLKEM768`.  
- **Pure PQC Algorithms**:  
  - ML-KEM (Kyber) for key encapsulation.  
  - ML-DSA (Dilithium) and SLH-DSA (Falcon) for digital signatures.  
- **Performance Metrics**:  
  - Execution time, energy consumption, memory usage, and bandwidth overhead.  
- **TLS 1.3 Integration**:  
  - Uses OpenSSL and the Open Quantum Safe (OQS) library for PQC support.  
- **Certificate Management**:  
  - Generate PQC and hybrid X.509 certificates for authentication.  

---

## **Project Structure**  
```plaintext  
pqc-tls-evaluation/  
├── src/: Core source code.  
│   ├── tls/: TLS handshake and PQC integration.  
│   ├── crypto/: Cryptographic algorithms (PQC, hybrid, traditional).  
│   ├── performance/: Tools for measuring time, energy, and memory.  
│   └── utils/: Certificate and logging utilities.  
├── tests/: Unit and integration tests.  
├── data/: Certificates and keys for testing.  
├── scripts/: Automation scripts (experiments, certificate generation).  
└── results/: Performance results (CSV files).  
```  

---

## **Prerequisites**  
- **Operating System**: Linux (Ubuntu 22.04 recommended) or macOS.  
- **Dependencies**:  
  - OpenSSL with PQC support ([OQS fork](https://github.com/open-quantum-safe/openssl)).  
  - Python 3.8+ with `psutil`, `matplotlib`, and `cryptography`.  
  - Intel RAPL (for energy measurement on Linux).  
  - Tools: `git`, `cmake`, `build-essential`.  

---

## **Installation**  
### 1. Install OpenSSL with PQC Support  
```bash  
# Clone and build OQS OpenSSL  
git clone https://github.com/open-quantum-safe/openssl.git  
cd openssl  
./Configure linux-x86_64 --prefix=/usr/local/oqs-openssl  
make  
sudo make install  
```  

### 2. Install Python Dependencies  
```bash  
pip install -r requirements.txt  
```  

### 3. Install Energy Measurement Tools (Linux)  
```bash  
sudo apt install powerstat  
```  

---

## **Usage**  

### **Generate Certificates**  
Generate traditional, PQC, and hybrid certificates:  
```bash  
chmod +x scripts/generate_certificates.sh  
./scripts/generate_certificates.sh  
```  

### **Run TLS Experiments**  
Test hybrid and pure PQC key exchanges:  
```bash  
# Example: Test X25519MLKEM768  
./scripts/run_tls_experiment.sh X25519MLKEM768  
```  

### **Performance Evaluation**  
Measure time, energy, and memory usage:  
```bash  
python scripts/evaluate_performance.py  
```  

---

## Usage Examples

### Running All Tests
To run all tests and verify your cryptographic and TLS modules:
```bash
pytest tests/
```

### Running a TLS Handshake Experiment
To run a hybrid TLS handshake and record the time taken:
```bash
chmod +x scripts/run_tls_experiment.sh
./scripts/run_tls_experiment.sh HybridKEM
```
This will append the result to `results/time_results.csv`.

### Generating Certificates
To generate traditional, PQC, and hybrid certificates:
```bash
chmod +x scripts/generate_certificates.sh
./scripts/generate_certificates.sh
```

### Analyzing Performance Results
To plot and analyze time, energy, and memory results:
```bash
python scripts/evaluate_performance.py
```

---

## Troubleshooting
- **python-oqs not installed:**
  - Ensure you have run `pip install -r requirements.txt` and that your Python environment is active.
- **OQS-OpenSSL not found:**
  - PQC and hybrid certificate generation requires OQS-OpenSSL. See https://github.com/open-quantum-safe/openssl for installation instructions.
- **Permission denied on scripts:**
  - Run `chmod +x scripts/*.sh` to make scripts executable.
- **Test failures:**
  - Ensure all dependencies are installed and you are running on Linux as recommended.
- **Performance scripts not plotting:**
  - Make sure `matplotlib` and `pandas` are installed and your results CSVs are not empty.

---

## **Performance Metrics**  
| Metric                | Tools Used                          | Output File          |  
|-----------------------|-------------------------------------|----------------------|  
| Execution Time        | Python `time` module                | `time_results.csv`   |  
| Energy Consumption    | Intel RAPL (`powerstat`)           | `energy_results.csv` |  
| Memory Usage          | `psutil`                            | `memory_results.csv` |  
| Bandwidth Overhead    | Wireshark/tcpdump (manual analysis) | N/A                  |  
---

## **References**  
- IETF Draft: [Post-Quantum Cryptography Recommendations for TLS-based Applications](https://datatracker.ietf.org/doc/draft-reddy-uta-pqc-app/).  
- NIST PQC Standardization: [ML-KEM, ML-DSA, SLH-DSA](https://csrc.nist.gov/projects/post-quantum-cryptography).  
- Open Quantum Safe: [liboqs](https://github.com/open-quantum-safe/liboqs).  

---
