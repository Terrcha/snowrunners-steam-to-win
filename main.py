import struct
import os

def decode_hash(hash_bytes):
    new_hash_bytes = bytearray()
    new_hash_bytes.append(hash_bytes[3])
    new_hash_bytes.append(hash_bytes[2])
    new_hash_bytes.append(hash_bytes[1])
    new_hash_bytes.append(hash_bytes[0])
    new_hash_bytes.append(hash_bytes[5])
    new_hash_bytes.append(hash_bytes[4])
    new_hash_bytes.append(hash_bytes[7])
    new_hash_bytes.append(hash_bytes[6])
    return new_hash_bytes.hex().upper() + hash_bytes[8:].hex().upper()

def parse_file_bytes(bytes, bypass_hash_check):
    filepath = bytes[:-32].decode("utf-16").strip("\x00")
    hash1 = decode_hash(bytes[-32:-16])
    hash2 = decode_hash(bytes[-16:])
    if hash1 != hash2:
        if not bypass_hash_check:
            raise ValueError(f"Inconsistent hash for {filepath}")
        if hash1 == "0" * 32:
            print(f"Warning: no hash check for {filepath}")
        else:
            print(f"Warning: hash check failed for {filepath}")
    return filepath, hash2

def load_saves(container_path, bypass_hash_check=False):
    save_files = []
    with open(container_path, "rb") as win_path:
        _header = struct.unpack("I", win_path.read(4))[0]
        numfiles = struct.unpack("I", win_path.read(4))[0]
        for i in range(numfiles):
            save_files.append(parse_file_bytes(win_path.read(160), bypass_hash_check))
    return save_files

def load_container(save_path):
    try:
        files = os.listdir(save_path)
        for file in files:
            if "container" in file:
                return file
        else:
            return "No container file found, please check windows save folder location"
    except Exception as error:
        print(error)   
    

def save_conversion():
    win_path = input("Enter path to windows save\n")
    steam_path = input("Enter path to steam save\n")

    container = load_container(save_path=win_path)
    container_path = f"{win_path}/{container}"
    load_saves(container_path)
    

if __name__ == "__main__":
    save_conversion()    


