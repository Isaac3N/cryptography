import hashlib
# TThis library takes a variable length of bytes and converts it into a fixed length sequence.
import time


transactions = []


def encrypt_transaction(hash_transaction):
    digital_signature = hashlib.sha256(hash_transaction.encode()).hexdigest()
    return digital_signature


def is_valid_signature(hash):
    if hash.startswith("0"):
        return True
    return False


def hash_transaction(data, timestamp, previoushash, index):
    _hash = ""
    nonce = 0
    while not is_valid_signature(_hash):
        _input = data + str(timestamp) + \
            str(previoushash) + str(index) + str(nonce)
        _hash = encrypt_transaction(_input)
        nonce += 1
        print(nonce)
    transactions.append(_hash)


def get_last_hash():
    return transactions[len(transactions)-1]


def add_new_transaction(message):
    _index = len(transactions)
    timestamp = time.time()
    previous_hash = get_last_hash
    hash_transaction(message, timestamp, previous_hash, _index)


def get_all_transactions():
    for i in range(0, len(transactions)):
        print(transactions[i])


def init_transaction():
    data = "Angie pays 100 dollars"
    timestamp = time.time()
    previous_hash = 0
    index = 0
    hash_transaction(data, timestamp, previous_hash, index)
