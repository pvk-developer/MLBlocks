Text Pipelines
==============

Here we will be showing some examples using **MLBlocks** to resolve text problems.

Text Classification
-------------------

For the text classification examples we will be using the `Twenty Newsgroups Dataset`_,
which we will load using the ``mlblocks.dataset.load_newsgroups`` function.

The data of this dataset is a 1d numpy array vector containing the texts from 11314 newsgroups
posts, and the target is a 1d numpy integer array containing the label of one of the 20 topics
that they are about.

MLPrimitives + Keras Preprocessing + Keras LSTM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example we will start by applying some text cleanup using the `TextCleaner primitive`_
from MLPrimitives, to then go into some `keras preprocessing` primitives and end
using a `Keras LSTM Classifier from MLPrimitives`_

.. code-block:: python

    import nltk
    from mlblocks import MLPipeline
    from mlblocks.datasets import load_newsgroups

    dataset = load_newsgroups()
    dataset.describe()

    X_train, X_test, y_train, y_test = dataset.get_splits(1)

    # Make sure that we have the necessary data
    nltk.download('stopwords')

    # Compute the vocabulary length.
    # This is required by the LSTM primitive
    vocabulary = set()
    pad_length = 0
    for text in X_train:
        words = text.split()
        pad_length = max(pad_length, len(words))
        vocabulary.update(words)

    primitives = [
        'mlprimitives.text.TextCleaner',
        'keras.preprocessing.text.Tokenizer',
        'keras.preprocessing.sequence.pad_sequences',
        'keras.Sequential.LSTMTextClassifier'
    ]
    init_params = {
        'mlprimitives.text.TextCleaner': {
            'language': 'en'
        },
        'keras.Sequential.LSTMTextClassifier': {
            'dense_units': 20,
            'pad_length': 100,
            'embedding_input_dim': len(vocabulary) + 1
        }
    }
    pipeline = MLPipeline(primitives, init_params)

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    dataset.score(y_test, predictions)


Tabular Data with Text
----------------------

For these examples examples we will be using the `Personae Dataset`_, which we will load
using the ``mlblocks.dataset.load_personae`` function.

The data of this dataset is a 2d numpy array vector containing 145 entries that include
texts written by Dutch users in Twitter, with some additional information about the author,
and the target is a 1d numpy binary integer array indicating whether the author was extrovert
or not.

MLPrimitives + Scikit-learn RandomForestClassifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example use again the `TextCleaner primitive`_, then use a `StringVectorizer primitive`_,
to encode all the string features, and go directly into the
`RandomForestClassifier from scikit-learn`_.

.. code-block:: python

    import nltk
    from mlblocks import MLPipeline
    from mlblocks.datasets import load_personae

    dataset = load_personae()
    dataset.describe()

    X_train, X_test, y_train, y_test = dataset.get_splits(1)

    # Make sure that we have the necessary data
    nltk.download('stopwords')

    primitives = [
        'mlprimitives.text.TextCleaner',
        'mlprimitives.feature_extraction.StringVectorizer',
        'sklearn.ensemble.RandomForestClassifier',
    ]
    init_params = {
        'mlprimitives.text.TextCleaner': {
            'column': 'text',
            'language': 'nl'
        },
        'sklearn.ensemble.RandomForestClassifier': {
            'n_jobs': -1,
            'n_estimators': 100
        }
    }
    pipeline = MLPipeline(primitives, init_params)

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    dataset.score(y_test, predictions)


.. _Twenty Newsgroups Dataset: http://scikit-learn.org/stable/datasets/twenty_newsgroups.html
.. _TextCleaner primitive: https://github.com/HDI-Project/MLPrimitives/blob/master/mlprimitives/text.py
.. _StringVectorizer primitive: https://github.com/HDI-Project/MLPrimitives/blob/master/mlprimitives/feature_extraction.py
.. _keras text preprocessing: https://keras.io/preprocessing/text/
.. _Keras LSTM Classifier from MLPrimitives: https://github.com/HDI-Project/MLPrimitives/blob/master/mlblocks_primitives/keras.Sequential.LSTMTextClassifier.json
.. _Personae Dataset: https://www.clips.uantwerpen.be/datasets/personae-corpus
.. _RandomForestClassifier from scikit-learn: http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
