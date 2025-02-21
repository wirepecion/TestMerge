import random

def generate_secret_number(length=4):
    """Generate a secret number with unique digits."""
    digits = list(range(10))
    random.shuffle(digits)
    secret_number = ''.join(map(str, digits[:length]))
    return secret_number

if __name__ == "__main__":
    print("Generated Secret Number:", generate_secret_number())