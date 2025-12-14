"""Fastapi app that servers prediction for Iris dataset """

import os
import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel


#Creating app
app=FastAPI()


# Base directory for model loading
BASE=os.path.dirname(os.path.abspath(__file__))
MODEL_PATH=os.path.join(BASE,"model","model.joblib")

# loading the trained Model
model=joblib.load(MODEL_PATH)


LABELS=['Setosa','Virginica','Versicolor']


class Irismodel(BaseModel):
    """schema for incoming predcition"""
    features : list[float]


@app.get('/')
def root():
    """Health check endpoint."""
    return {'Health':'OK'}

@app.post('/predict')
def prediciton(data:Irismodel):

    """Predict the class of an Iris flower based on features."""

    x=np.array([data.features])
    pred=int(model.predict(x)[0])

    return {
        'class_index' : pred,
        'class_name':LABELS[pred]
    }