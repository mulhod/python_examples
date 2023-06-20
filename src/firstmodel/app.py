import joblib

from fastapi import FastAPI
from firstmodel import version
from firstmodel.models import TextRequest
from firstmodel.run_experiment import predict

app: FastAPI = FastAPI(
    title="MyAPI",
    version=version,
    docs_url=None,
    redoc_url=None,
)


@app.get("/info")
def some_function():
    return version


@app.post("/predict")
def text_predict(request: TextRequest):
    model = joblib.load(open("/python_examples/model1/model", "rb"))
    vec = joblib.load(open("/python_examples/model1/vectorizer", "rb"))
    return predict(request.text, model, vec)
