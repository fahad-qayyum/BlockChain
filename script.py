from blockchain import Blockchain

# 3 transactions
block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}

# making a fake transacation 
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}
local_blockchain = Blockchain()
local_blockchain.print_blocks()

# adding blocks to my block_chain 
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)

# checking if the chain is valid and printing
local_blockchain.validate_chain()
local_blockchain.print_blocks()
