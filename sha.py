from hashlib import sha256

MAX_NONCE = 1000000


def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined bitcoin with nonce values:{nonce}")
            return new_hash

    raise BaseException(f"Could not find correct after trying{MAX_NONCE}")

if __name__=='__main__':
    transactions = """
    Bob->Denis->20
    Joe->Vince->50
    """
    difficulty = 4
    import time
    start = time.time()
    print("miner started..")
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)


