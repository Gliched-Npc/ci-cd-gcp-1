"""Testing If Model exists or not """

import os

def test_model_exist():
    """
    checks if a model file named `model.joblib` exists in the `model`
    directory.
    """
    assert os.path.exists('model/model.joblib'),"Model Missing"