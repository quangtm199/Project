import io
import os
import unittest

from magpie import Magpie
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'hep-categories')

with io.open(DATA_DIR + '.labels', 'r') as f:
    labels = [line.rstrip('\n') for line in f]
    labels=list(set(labels))
print(len(labels))
k="";
for i in range(len(labels)):
    k=k+str(labels[i])+"\n"
print(k);
f=io.open(DATA_DIR + '.labels', 'w')
f.write(k)