# Code Signing and Validator Project

## Overview
This project shows how to use digital signatures to keep software safe. We use a method called code signing. In this project, a software vendor (the developer) creates a product that prints a message with a student ID. The vendor then signs the product using a secret key with the Elliptic Curve Digital Signature Algorithm (ECDSA). The user can check the signature with a public key. If the signature is correct, the product runs; if not, the execution is blocked.

## Features
- **Key Generation:** Creates a pair of keys (private and public) using ECDSA.
- **Product Program:** Prints a simple message that includes a student ID.
- **Digital Signing:** Signs the product using the secret (private) key.
- **Signature Verification:** A validator checks the signature with the public key. Execution is allowed only if the signature is valid.
- **Attack Simulation:** Demonstrates that if the product is changed (by adding malicious code), the validator will block its execution.

## Requirements
- Python 3.x
- The `ecdsa` library  
  Install it with:
  ```bash
  pip install ecdsa

```markdown
# Digital Signature Project: Secure Software Execution

## Installation Steps

1. **Install Python 3.x**: Ensure Python is installed on your computer.
2. **Install Dependencies**: Open your terminal or command prompt and run:
   ```bash
   pip install ecdsa
   ```
3. **Download the Code**: Download or clone the project code to your computer.

## Project Structure

- **`product_program.py`**: The main Python script that:
  - Checks for existing keys or generates new ECDSA keys.
  - Creates a product program that prints "I am a software made by [Student ID]".
  - Signs the product program.
  - Validates the signature using a validator.
  - Simulates an attack by modifying the product to show that the signature fails.

- **`private_key.pem`**: File storing the private key (generated automatically).
- **`public_key.pem`**: File storing the public key (generated automatically).
- **`program_signature.sig`**: File storing the digital signature (generated automatically).

## How to Run the Project

1. Open your terminal or command prompt.
2. Change the directory to where the project files are located.
3. Run the following command:
   ```bash
   python product_program.py
   ```
   The script will:
   - Generate and display the keys.
   - Print the product program message.
   - Sign the product.
   - Verify the signature and print "Code certificate valid: execution allowed" if valid.
   - Simulate an attack by adding malicious code, causing the validator to print "Code certificate invalid: execution denied".

## How the Code Works

### Key Generation
- The script checks if key files exist. If not, it generates a new key pair using the **SECP256k1** curve and saves them as PEM files.

### Product Program
- A simple string that prints "I am a software made by [Student ID]". Replace `[Student ID]` with your actual student ID.

### Digital Signing
- The script calculates a **SHA-256 hash** of the product program and signs this hash using the private key. The resulting signature is stored in a file.

### Signature Verification
- The validator reads the public key and checks the signature against the hash of the product program. If they match, it confirms the product is genuine and safe to run.

### Attack Simulation
- The script modifies the product by adding a line that prints "Malicious code!" which causes the signature verification to fail. This demonstrates how tampered software is blocked.

## Demo Video

A demonstration video of this project is available. The video explains:
- How code signing works.
- How keys are generated.
- How the product is signed.
- How the validator checks the signature.
- What happens when the product is tampered with.

You can watch the video here: [Your Demo Video Link]

## Conclusion

This project demonstrates how digital signatures protect software from tampering. By signing the product and verifying its signature, we ensure that only genuine and unaltered code is executed, which is essential for software security.

## Contact Information

If you have any questions or suggestions, please contact:

- **Name**: [Your Name]
- **Email**: [Your Email]
```