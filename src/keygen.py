import os
from ecdsa import SigningKey, SECP256k1

def generate_keys(private_path='keys/private_key.pem', public_path='keys/public_key.pem'):
    if not os.path.exists(private_path) or not os.path.exists(public_path):
        os.makedirs(os.path.dirname(private_path), exist_ok=True)
        private_key = SigningKey.generate(curve=SECP256k1)
        public_key = private_key.get_verifying_key()

        with open(private_path, 'wb') as priv_file:
            priv_file.write(private_key.to_pem())
        with open(public_path, 'wb') as pub_file:
            pub_file.write(public_key.to_pem())

        print("Keys generated and saved.")
    else:
        print("Keys already exist.")
