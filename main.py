
import hashlib

def calculate_checksums(file_path):
        md5_hash = hashlib.md5()
        sha256_hash = hashlib.sha256()
        sha512_hash = hashlib.sha512()

        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
                sha256_hash.update(byte_block)
                sha512_hash.update(byte_block)

        print(f"MD5: {md5_hash.hexdigest()}")
        print(f"SHA256: {sha256_hash.hexdigest()}")
        print(f"SHA512: {sha512_hash.hexdigest()}")

file_path = input("Enter the file path: ")
calculate_checksums(file_path)
