from block import Block
from datetime import datetime
from crypt import crypt
from pprint import pprint

class Blockchain:

    def __init__(self):
        self.blocks = []
        Genesis = Block(transactions="Bloco Genesis Bolado!",
                        index=0, previous_hash=0, timestamp=datetime.utcnow().timestamp())
        self.blocks.append(crypt(Genesis))

    def previous_hash(self):
        return self.blocks[-1]

    def add(self, transaction):
        block = Block(transactions=transaction,
                      index=len(self.blocks),
                      previous_hash=self.previous_hash(),
                      timestamp=datetime.utcnow().timestamp())
        hashed_block = crypt(block)
        self.blocks.append(hashed_block)

    def list(self):
        pprint(self.blocks)

    def valid(self):
        return all(_hash.startswith("000") for _hash in self.blocks)
