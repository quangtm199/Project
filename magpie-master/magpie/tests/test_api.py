import io
import os
import unittest

from magpie import Magpie
import pickle
# This one is hacky, but I'm too lazy to do it properly!
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'hep-categories')
print(PROJECT_DIR)
class TestAPI(unittest.TestCase):
	""" Basic integration test """
	def test_cnn_train(self):
		# Get them labels!
		print(PROJECT_DIR)
		print(DATA_DIR)
		with io.open(DATA_DIR + '.labels', 'r') as f:
			labels = [line.rstrip('\n') for line in f]
			labels=list(set(labels))


		# Run the model

		model = Magpie()
		a=model.train_word2vec(DATA_DIR, vec_dim=300)
		print("done2")

		print("done3")
		model.init_word_vectors(DATA_DIR, vec_dim=300)
		model.train(DATA_DIR, labels, nn_model='cnn', test_ratio=0.2, epochs=30)
		path1 = PROJECT_DIR + '/here1.h5'
		path2 = PROJECT_DIR + '/embedinghere'
		path3 = PROJECT_DIR + '/scaler'
		model.save_word2vec_model(path2)
		model.save_scaler(path3, overwrite=True)
		model.save_model(path1)
		print("thuc hien test")

		# Do a simple prediction

		print(model.predict_from_text('cho em hỏi về lịch khám của bác_sỹ đào việt_hằng và số điện_thoại'))




