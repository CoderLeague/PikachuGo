# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright 2018 The YouDao Authors. All Rights Reserved.
             2020 NetEase, YouDao (author: Wang Yulong)
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================
"""

import numpy as np
import pandas as pd

import sys, random

#reload(sys)
#sys.setdefaultencoding('utf8')

import time, os, json, math, re
import threading, logging, copy, scipy
from datetime import datetime, timedelta
import collections
import argparse

script_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_root)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("ERROR use python script.")
        print("Usage: python ***.py lexicon.txt oov_words.txt output.txt")
        print("lexicon.txt: 文件每一行的格式是 'word phone1 phone2 phone3 ...'")
        print("oov_words.txt: 文件每一行的格式是 'oov_word'")
        print("output.txt: 将搜索的结果输出致该文件")
    else:
        [lexicon_file, oov_words_file, output_file] = sys.argv[1:]
        