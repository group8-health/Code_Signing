import hashlib
from ecdsa import SigningKey
import os

def sign_program(program_code, private_key_path='keys/private_key.pem', signature_path='signatures/program_signature.sig'):
    with open(private_key_path, "rb") as priv_file:
        private_key = SigningKey.from_pem(priv_file.read())

    program_hash = hashlib.sha256(program_code.encode('utf-8')).digest()
    signature = private_key.sign(program_hash)

    os.makedirs(os.path.dirname(signature_path), exist_ok=True)
    with open(signature_path, "wb") as sig_file:
        sig_file.write(signature)

    print("Program signed.")
    print("Signature (hex):", signature.hex())
