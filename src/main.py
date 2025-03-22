from keygen import generate_keys
from product import get_product_program
from signer import sign_program
from validator import verify_signature

def main():
    # Generate Keys
    generate_keys()

    # Create Product
    student_id = "1234567890"
    product_code = get_product_program(student_id)
    print("\nProduct Program:\n", product_code)

    # Sign the Product
    sign_program(product_code)

    # Verify Original Product
    print("\nVerifying Original Program (Valid):")
    is_valid = verify_signature(product_code)
    print("Validation result:", is_valid)

    # Simulate Malicious Modification
    malicious_code = product_code + "\nMalicious code!"
    print("\nVerifying Modified Program (Malicious Code):")
    is_valid_malicious = verify_signature(malicious_code)
    print("Validation result:", is_valid_malicious)

if __name__ == "__main__":
    main()
