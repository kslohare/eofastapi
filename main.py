from typing import Union
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing_extensions import Annotated


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items/")
async def create_item(item: Item):
    # print("create_item called..")
    # print(item)
    return item


@app.post("/files/")
async def create_file(file: Annotated[Union[bytes, None], File()] = None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/upload-file/")
async def create_upload_file(file: Union[UploadFile, None] = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}
