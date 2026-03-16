import hashlib
import json
import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        block = {
            "index": 0,
            "timestamp": time.time(),
            "data": "Genesis Block",
            "previous_hash": "0",
            "hash": self.hash_block(0, time.time(), "Genesis Block", "0")
        }
        self.chain.append(block)

    def create_block(self, data):
        previous_block = self.chain[-1]
        index = len(self.chain)
        timestamp = time.time()
        previous_hash = previous_block["hash"]
        block_hash = self.hash_block(index, timestamp, data, previous_hash)

        block = {
            "index": index,
            "timestamp": timestamp,
            "data": data,
            "previous_hash": previous_hash,
            "hash": block_hash
        }

        self.chain.append(block)
        return block

    def hash_block(self, index, timestamp, data, previous_hash):
        block_string = json.dumps(
            {"index": index, "timestamp": timestamp, "data": data, "previous_hash": previous_hash},
            sort_keys=True
        ).encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_chain(self):
        return self.chain
