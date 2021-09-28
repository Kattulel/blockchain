from block import Block
from datetime import datetime
from miner import mine
import random, string

Genesis = Block(transactions="Bloco Genesis Bolado!", index=0, previous_hash=0, timestamp=str(datetime.now()))
_hash, nonce = mine(Genesis)
current = Genesis
for i in range(1, 5):
    mensagem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
    current.next = Block(transactions=f'{mensagem}', index=current.next_index(), previous_hash=_hash, timestamp=str(datetime.now()), nonce=1)
    current = current.next
    _hash, nonce = mine(current)
    current.nonce = nonce

Genesis.print()
