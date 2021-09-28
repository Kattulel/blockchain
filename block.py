from pprint import pprint

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=1):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.previous = None
        self.nonce = nonce

    def print(self):
        pprint({"index": self.index,
                "transactions": self.transactions,
                "timestamp": self.timestamp,
                "previous_hash": self.previous_hash,
                "nonce": self.nonce
                })

    def str(self):
        return f'{self.transactions}{self.nonce}{self.index}{self.timestamp}{self.previous_hash}'.encode("utf-8")
