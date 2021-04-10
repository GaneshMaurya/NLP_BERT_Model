# NLP with BERT for Sendtiment Analysis

!pip3 install ktrain

# Import Libraries

import os.path
import numpy as np
import tensorflow as tf
import ktrain
from ktrain import text

# Data Preprocessing

# Loading the IMDB dataset

dataset = tf.keras.utils.get_file(fname = 'aclImdb_v1.tar.gz',
                                  origin = 'http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz',
                                  extract = True)
IMDB_DATADIR = os.path.join(os.path.dirname(dataset), 'aclImdb')

print(os.path.dirname(dataset))
print(IMDB_DATADIR)

# Training and Test Set

(X_train, y_train), (X_test, y_test), preproc = text.texts_from_folder(datadir = IMDB_DATADIR,
                                                                       classes = ['pos', 'neg'],
                                                                       maxlen = 500,
                                                                       train_test_names = ['train', 'test'],
                                                                       preprocess_mode = 'bert')


# Building the BERT model

model = text.text_classifier(name = 'bert',
                             train_data = (X_train, y_train),
                             preproc = preproc)


# Training the BERT model

learner = ktrain.get_learner(model = model,
                             train_data = (X_train, y_train),
                             val_data = (X_test, y_test),
                             batch_size = 6)

learner.fit_onecycle(lr = 2e-5, epochs = 1)