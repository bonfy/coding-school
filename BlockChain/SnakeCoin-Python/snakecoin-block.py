# -*- coding:utf-8 -*-

###
# Author: bonfy
# Email: foreverbonfy@163.com
# Created Date: 2018-02-01
###

import hashlib as hasher
import datetime as date


class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        seq = (str(x) for x in (
               self.index, self.timestamp, self.data, self.previous_hash))
        sha.update(''.join(seq).encode('utf-8'))
        return sha.hexdigest()


def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), 'Genesis Block', '0')


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = 'Hey! I\'m block ' + str(this_index)
    this_previous_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_previous_hash)


if __name__ == '__main__':

    # Create the blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    # How many blocks should we add to the chain
    # after the genesis block
    num_of_blocks_to_add = 20

    # Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add

        # Tell everyone about it!
        print('Block #{} has been added to the blockchain!'.format(
            block_to_add.index))
        print(f'Data: {block_to_add.data} Timestamp: {block_to_add.timestamp}')
        print('Hash: {}\n'.format(block_to_add.hash))
