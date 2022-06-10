from fastapi import FastAPI, File
from nsfw_detector import predict
from random import randint
import os

model = predict.load_model('./mobilenet/saved_model.h5')

app = FastAPI()

@app.post("/is_nsfw")
def read_root(name: str = None, file: bytes | None = File(default=None)):
    if not file:
        return {"status_code": "fail", "status": "Файл не загружен"}
    
    if not name:
        return {"status_code": "fail", "status": "Добавьте информацию о названии файла"}
    
    name = f"{randint(0,100000)}{os.path.splitext(name)[1]}"
    with open(name, "wb") as f:
        f.write(file)
    
    answer = predict.classify(model, name)
    os.remove(name)
    return {"status_code": "succesful", "status": "Удачно", "answer": answer[name]}
