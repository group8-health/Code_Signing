import hashlib
from ecdsa import VerifyingKey, BadSignatureError

def verify_signature(program_code, signature_file='signatures/program_signature.sig', public_key_path='keys/public_key.pem'):
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
