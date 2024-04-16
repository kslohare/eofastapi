from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, 'Computer Science Pro1', 'author1', 'nice book1', 5),
    Book(2, 'Computer Science Pro2', 'author2', 'nice book2', 4),
    Book(3, 'Computer Science Pro3', 'author3', 'nice book3', 3),
    Book(4, 'Computer Science Pro4', 'author4', 'nice book4', 2),
    Book(5, 'Computer Science Pro5', 'author5', 'nice book5', 1)
]


class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create_book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(new_book)
