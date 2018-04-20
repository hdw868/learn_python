# coding:utf-8
import os
files = os.listdir('.')

files = [fname.encode('gbk') for fname in files]
