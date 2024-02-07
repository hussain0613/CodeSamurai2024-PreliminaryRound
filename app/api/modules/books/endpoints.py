from typing import Literal

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session
from app.db_utils import engine


from .model import Book as BookDB
from .schema import Book, BookCreate, BookUpdate, BookSearch, BookListResponse

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", status_code=201)
def create_book(book: BookCreate) -> Book:
    """
    Adds a book to the library
    """
    with Session(engine) as session:
        bookdb: BookDB = BookDB(**book.model_dump(exclude_unset=True))
        session.add(bookdb)
        session.commit()
        session.refresh(bookdb)

        book_response: Book = Book.model_validate(bookdb)
        
    return book_response



@router.put("/{id}/")
def update_book(id: int, book: BookUpdate) -> Book:
    with Session(engine) as session:
        bookdb: BookDB = session.query(BookDB).get(id)
        if not bookdb:
            msg_dict = {"message": f"book with id: {id} was not found"}
            return JSONResponse(msg_dict, status_code=404)
        data_dict: dict = book.model_dump(exclude_unset=True)
        for field in data_dict:
            setattr(bookdb, field, data_dict[field])
        
        session.commit()
        book_response: Book = Book.model_validate(bookdb)

    return book_response




@router.get("/{id}/")
def read_book(id: int) -> Book:
    with Session(engine) as session:
        book_db: BookDB = session.query(BookDB).get(id)
        if not book_db:
            msg_dict = {"message": f"book with id: {id} was not found"}
            return JSONResponse(msg_dict, status_code=404)
        book: Book = Book.model_validate(book_db)
        
    return book




@router.get("/")
def read_books() -> BookListResponse:
    """
    Returns all the books.
    """
    with Session(engine) as session:
        books: list[Book] = [Book.model_validate(book) for book in session.query(BookDB).all()]
    
    return BookListResponse(books = books)




SORTING_OPTIONS = Literal["id", "title", "author", "genre", "price"]
ORDER_OPTIONS = Literal["ASC", "DESC"]
@router.get("/search/")
def search_books(query: BookSearch = Depends(BookSearch), sort: SORTING_OPTIONS = "id", order: ORDER_OPTIONS = "ASC") -> BookListResponse:
    """
    Search Books
    """
    with Session(engine) as session:
        order_by = BookDB.id
        if sort == "id":
            pass
        elif sort == "title":
            order_by = BookDB.title
        elif sort == "author":
            order_by = BookDB.author
        else:
            order_by = BookDB.price
        
        if order == "ASC":
            order_by = order_by.asc()
        else:
            order_by = order_by.desc()

        print(query)
        books_db = session.query(BookDB).filter_by(
            **query.model_dump(exclude_none=True)
        ).order_by(order_by)
        
        if sort != "id":
            books_db.order_by(BookDB.id.asc())
        
        books_db: list[BookDB] = books_db.all()

        books: list[Book] = [Book.model_validate(book) for book in books_db]

        return BookListResponse(books = books)


