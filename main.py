import blockchain as blockchain

if __name__ == "__main__":
    blockchain.init_block()
    blockchain.add_new_block("Christina Pays 100 dollars")
    blockchain.add_new_block("Charles Receives 20 dollars")
    blockchain.get_all_blocks()
