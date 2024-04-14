from typing import Union
from fastapi import FastAPI, File, UploadFile, Body
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
    {'tital': 'Tital Two', 'author': 'author one', 'category': 'science'},
    {'tital': 'Tital Three', 'author': 'author two', 'category': 'science'},
    {'tital': 'Tital Four', 'author': 'author three', 'category': 'math1'},
    {'tital': 'Tital Five', 'author': 'author four', 'category': 'math2'},
]


@app.get("/books")
async def fist_api():
    return BOOKS


@app.get("/books/{book_tital}")
async def read_book(book_tital: str):
    for book in BOOKS:
        if book.get('tital').casefold() == book_tital.casefold():
            return book


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/books/create_book")
async def create_book(new_book=Body()):  # Here Body() converts to new book
    BOOKS.append(new_book)
    return "Book has been added"


@app.put("books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('tital').casefold() == updated_book.get('tital').casefold():
            BOOKS[i] = updated_book
            return 'book is updated'


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
