# coding=utf-8

import os
import config
from pybloomfilter import BloomFilter
from b2.object2 import Singleton


class SpiderUrlFilter(Singleton):

    def __init__(self):
        bc = config.get_boolmfilter_config()
        if os.path.exists(bc['bin_path']):
            self.bloomfilter = BloomFilter.open(bc['bin_path'])
        else:
            self.bloomfilter = BloomFilter(
                bc['capacity'], bc['wrong_rate'], bc['bin_path'])

    def get_boolmfilter():
        bc = config.get_boolmfilter_config()
        if os.path.exists(bc['bin_path']):
            return BloomFilter.open(bc['bin_path'])
        else:
            return BloomFilter(bc['capacity'], bc['wrong_rate'], bc['bin_path'])



if __name__ == '__main__':
    pass
