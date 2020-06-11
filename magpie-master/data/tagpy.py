import io
import os
import unittest

from magpie import Magpie
dir_path = os.path.dirname(os.path.realpath(os.getcwd()))
dir_path = os.path.join(dir_path, 'data')
print(dir_path)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(dir_path,'hep-categories')

with io.open(DATA_DIR + '.labels', 'r') as f:
    labels = [line.rstrip('\n') for line in f]
    labels=list(set(labels))
with io.open(DATA_DIR + '.labels', 'w') as f:
    a="\n".join(labels)
    f.write(a)
print(len(labels))
print(labels)



