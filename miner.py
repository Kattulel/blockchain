from hashlib import sha256
from block import Block

def crypt(bloco: Block):
    b_hash = sha256(bloco.str())
    return b_hash.hexdigest()

def valid(b_hash):
    return True if str(b_hash).startswith("000") else False

def mine(original):
    result = crypt(original)
    if not valid(result):
        while not valid(result):
            original.nonce += 1
            result = crypt(original)
        print(f'[nonce] {original.nonce}')
        print(result)
    return result, original.nonce