import hashlib
# TThis library takes a variable length of bytes and converts it into a fixed length sequence.
import time


blocks = []  # A block is where all the information about the transaction is stored

# A function to create the genesis block of the blockchain


def init_block():
    transaction = "Angie Receives 100 dollars"
    timestamp = time.time()
    previous_hash = 0
    index = 0
    hash_transaction(transaction, timestamp, previous_hash, index)


# A function to hash the transaction made
def encrypt_transaction(hash_transaction):
    digital_signature = hashlib.sha256(hash_transaction.encode()).hexdigest()
    return digital_signature

# Checks whether the hash for the transaction is valid. The transaction is valid if the hash starts with 3 zeros the higher the number of zeros the higher the difficulty


def is_valid_hash(hash):
    if hash.startswith("00"):
        return True
    return False

# The hash_transaction takes all the block's data and creates a hash.


def hash_transaction(transaction, timestamp, previoushash, index):
    _hash = ""
    nonce = 0
    # We encrypt the hash and check whether the hash is valid. The hash needs to start with 3 0's
    # if the hash is not valid the nonce is incremented by 1
    while not is_valid_hash(_hash):
        _input = transaction + str(timestamp) + \
            str(previoushash) + str(index) + str(nonce)
        _hash = encrypt_transaction(_input)
        nonce += 1
        print(nonce)
    blocks.append(_hash)

# Calls the last block in the blockchain. A change in one block of the blockchain affects every other block in the blockcahin creating an avalanche effect


def get_last_hash():
    return blocks[len(blocks)-1]

# This function is used to add a block to the blockchain which is dependent on the previous hash


def add_new_block(transaction):
    _index = len(blocks)
    timestamp = time.time()
    previous_hash = get_last_hash
    hash_transaction(transaction, timestamp, previous_hash, _index)

# returns all the blocks in the blockchain


def get_all_blocks():
    for i in range(0, len(blocks)):
        print(blocks[i])
