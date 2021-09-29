import random
import string

class Miner:

    def __init__(self, bc_ref):
        self.bc_ref = bc_ref

    def mine(self, interations: int):
        for i in range(interations):
            mensagem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
            self.bc_ref.add(mensagem)
