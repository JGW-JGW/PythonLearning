# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-01 21:57
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod
from collections import OrderedDict

"""
OrderedDict
"""

if __name__ == '__main__':
    ordered_dict = OrderedDict()
    il = [
        ('b', 2),
        ('c', 3),
        ('d', 4),
        ('a', 1)
    ]
    for t in il:
        ordered_dict[t[0]] = t[1]

    pprint(ordered_dict)

    # 仅仅是一个字典的元素之间的顺序关系与插入顺序保持一致，而不是自动排序的字典
