import hashlib

def hash_password(password: str) -> str:
    # Create a new sha256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the bytes of the password
    sha256.update(password.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hashed_password = sha256.hexdigest()
    
    return hashed_password

# Example usage
if __name__ == "__main__":
    password = "my_secure_password"
    print(f"Original password: {password}")
    print(f"Hashed password: {hash_password(password)}")