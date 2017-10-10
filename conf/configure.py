#!/usr/local/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-10-10 下午7:36
"""
from __future__ import absolute_import, division, print_function

import os
import sys

module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)

class Configure(object):
    """ global configuration """

    positive_data_file = '../input/rt-polarity.pos'
    negative_data_file = '../input/rt-polarity.neg'