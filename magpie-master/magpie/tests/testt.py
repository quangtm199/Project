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
print(labels)
path1=PROJECT_DIR+'/here1.h5'
path2=PROJECT_DIR+'/embedinghere'
path3=PROJECT_DIR+'/scaler'

magpie = Magpie(
    keras_model=path1,
    word2vec_model=path2,
    scaler=path3,
    labels=labels

)

predictions = magpie.predict_from_text('toi bi dau bung kham benh het bao nhieu tien')
print(predictions[0],predictions[1],predictions[2])