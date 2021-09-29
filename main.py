from block_chain import Blockchain
from miner import Miner

blockchain = Blockchain()
# blockchain.add("oi")
# blockchain.add("tudo")
# blockchain.add("bem")

miner = Miner(blockchain)

miner.mine(7)

blockchain.list()

print(blockchain.valid())


