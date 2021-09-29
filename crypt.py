from hashlib import sha256
from block import Block

def do_hash(bloco: Block):
    b_hash = sha256(bloco.str())
    return b_hash.hexdigest()

def valid(b_hash):
    return str(b_hash).startswith("000")

def crypt(original):
    result = do_hash(original)
    if not valid(result):
        while not valid(result):
            original.nonce += 1
            result = do_hash(original)
        print(f'[nonce] {original.nonce}')
    return result
