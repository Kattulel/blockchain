from block import Block
from datetime import datetime
from miner import mine

Genesis = Block(transactions="Mensagem", index=0, previous_hash=0, timestamp=str(datetime.now()))
_hash = mine(Genesis)
for i in range(5):
    original = Genesis
    Genesis = Block(transactions=f'Mensagem{i}', index=original.index+1, previous_hash=_hash, timestamp=str(datetime.now()))
    Genesis.previous = original
    _hash = mine(Genesis)

print(Genesis)