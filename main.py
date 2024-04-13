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

# Create List of books
BOOKS = [
    {'tital': 'Tital One', 'author': 'author one', 'category': 'science'},
    {'tital': 'Tital One', 'author': 'author one', 'category': 'science'},
    {'tital': 'Tital One', 'author': 'author two', 'category': 'science'},
    {'tital': 'Tital One', 'author': 'author three', 'category': 'math1'},
    {'tital': 'Tital One', 'author': 'author four', 'category': 'math2'},
]


@app.get("/books")
async def fist_api():
    return BOOKS


@app.get("/books/{book_total}")
async def read_book(book_total: str):
    for book in BOOKS:
        if book.get('total').casefold() == book_total.casefold():
            return book


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
