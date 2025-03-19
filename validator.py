"""
Product Program and Validator using ECDSA Signature Verification

This script demonstrates code signing and validation using ECDSA. It simulates
a software vendor signing a product and a user validating the product's integrity.
If the digital signature is valid, execution is allowed; if invalid, execution is denied.

Usage:
    python product_program.py

Dependencies:
    - ecdsa (install via: pip install ecdsa)
"""

import os
import hashlib
from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError

# -------------------------------
# Step 1: Generate ECDSA Keys
# -------------------------------
def generate_keys():
    """
    Generates an ECDSA private/public key pair, saves them to files,
    and prints the PEM-formatted keys.
    """
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    
    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(private_key.to_pem())
    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(public_key.to_pem())
    
    print("Keys generated and saved.")
    print("\n--- Private Key (PEM format) ---")
    print(private_key.to_pem().decode('utf-8'))
    print("\n--- Public Key (PEM format) ---")
    print(public_key.to_pem().decode('utf-8'))

# Generate keys only if they do not exist already
if not (os.path.exists("private_key.pem") and os.path.exists("public_key.pem")):
    generate_keys()
else:
    print("Keys already exist. Displaying the keys:")
    with open("private_key.pem", "rb") as priv_file:
        print("\n--- Private Key (PEM format) ---")
        print(priv_file.read().decode('utf-8'))
    with open("public_key.pem", "rb") as pub_file:
        print("\n--- Public Key (PEM format) ---")
        print(pub_file.read().decode('utf-8'))

# -------------------------------
# Step 2: Prepare the Product Program
# -------------------------------
def get_product_program(student_id):
    """
    Returns the product program as a string.
    Replace [Student ID] with your actual student ID.
    """
    return f"I am a software made by {student_id}"

# Student-ID
student_id = "1234567890"
product_code = get_product_program(student_id)
print("\nProduct Program:")
print(product_code)

# -------------------------------
# Step 3: Sign the Product Program
# -------------------------------
def sign_program(program_code, private_key_path):
    """
    Signs the program code using the ECDSA private key.
    The signature is saved in 'program_signature.sig' and printed in hexadecimal.
    """
    with open(private_key_path, "rb") as priv_file:
        private_key = SigningKey.from_pem(priv_file.read())
    
    # Create a SHA-256 
    program_hash = hashlib.sha256(program_code.encode('utf-8')).digest()
    signature = private_key.sign(program_hash)
    
    with open("program_signature.sig", "wb") as sig_file:
        sig_file.write(signature)
    
    print("\nProgram signed and signature saved as 'program_signature.sig'.")
    print("Signature (hex):", signature.hex())

# Private_Key
sign_program(product_code, "private_key.pem")

# -------------------------------
# Step 4: Validate the Signature (Validator)
# -------------------------------
def verify_signature(program_code, signature_file, public_key_path):
    """
    Verifies the digital signature of the program code.
    Prints whether execution is allowed or denied.
    """
    with open(public_key_path, "rb") as pub_file:
        public_key = VerifyingKey.from_pem(pub_file.read())
    
    program_hash = hashlib.sha256(program_code.encode('utf-8')).digest()
    
    with open(signature_file, "rb") as sig_file:
        signature = sig_file.read()
    
    try:
        if public_key.verify(signature, program_hash):
            print("Code certificate valid: execution allowed")
            return True
        else:
            print("Code certificate invalid: execution denied")
            return False
    except BadSignatureError:
        print("Code certificate invalid: execution denied")
        return False

# -------------------------------
# Step 5: Validate the Original Product
# -------------------------------
print("\nVerifying Original Program (Valid):")
is_valid = verify_signature(product_code, "program_signature.sig", "public_key.pem")
print("Validation result:", is_valid)

# -------------------------------
# Step 6: Simulate an Attack (Modify the Product)
# -------------------------------
malicious_code = product_code + "\nMalicious code!"
print("\nVerifying Modified Program (Malicious Code):")
is_valid_malicious = verify_signature(malicious_code, "program_signature.sig", "public_key.pem")
print("Validation result for malicious code:", is_valid_malicious)

if __name__ == '__main__':
    pass
