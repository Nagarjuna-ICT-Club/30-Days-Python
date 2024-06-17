import hashlib

plain_text = 'The guards will go have dinner at 8pm'
byte_text = plain_text.encode('utf-8')

hash_obj = hashlib.sha256()

# Update the hash object with data
hash_obj.update(byte_text)

hex_digest = hash_obj.hexdigest()
print(hex_digest)

# digest() returns digest as a byte string
byte_digest = hash_obj.digest()
print(byte_digest)
