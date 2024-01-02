from typing import Union
from fastapi import FastAPI
from uce.ai.openaitest import Document, inference

app = FastAPI()

@app.post('/inference', status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)


    binary_result = ''.join([char for char in response[0] if char in '01'])

    return {
        'binary': binary_result,
        'usage': response[1]
    }


