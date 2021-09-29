
class Block:
    def __init__(self, transactions, timestamp, previous_hash, nonce=1, index=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def str(self):
        return f'{self.transactions}{self.nonce}{self.index}{self.timestamp}{self.previous_hash}'.encode("utf-8")