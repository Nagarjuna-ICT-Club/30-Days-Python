import hashlib

# Plaintext to be hashed
plain_text = 'Hello from NICT Club'

# The hash functions requires bytes
# instead of a string
byte_text = plain_text.encode('utf-8')

# Create a `sha1` hash object
hash_obj = hashlib.sha1(byte_text)

# hexdigest() returns the digest as
# a hexadecimal string 
cipher_text = hash_obj.hexdigest()

print(cipher_text)