import hashlib
# TThis library takes a variable length of bytes and converts it into a fixed length sequence.
import time


blocks = []


def encrypt_transaction(hash_transaction):
    digital_signature = hashlib.sha256(hash_transaction.encode()).hexdigest()
    return digital_signature


def is_valid_signature(hash):
    if hash.startswith("0"):
        return True
    return False


def hash_transaction(transaction, timestamp, previoushash, index):
    _hash = ""
    nonce = 0
    while not is_valid_signature(_hash):
        _input = transaction + str(timestamp) + \
            str(previoushash) + str(index) + str(nonce)
        _hash = encrypt_transaction(_input)
        nonce += 1
        print(nonce)
    blocks.append(_hash)


def get_last_hash():
    return blocks[len(blocks)-1]


def add_new_block(transaction):
    _index = len(blocks)
    timestamp = time.time()
    previous_hash = get_last_hash
    hash_transaction(transaction, timestamp, previous_hash, _index)


def get_all_blocks():
    for i in range(0, len(blocks)):
        print(blocks[i])


def init_block():
    transaction = "Angie Receives 100 dollars"
    timestamp = time.time()
    previous_hash = 0
    index = 0
    hash_transaction(transaction, timestamp, previous_hash, index)
