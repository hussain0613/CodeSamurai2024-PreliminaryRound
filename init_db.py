from app.db_utils import Base, engine

# Import the models to create the tables

# For example, if we have a books module with a Book model
from app.api.modules.books.model import Book

if __name__ == "__main__":

    Base.metadata.create_all(bind=engine)
    print("Database initialized!")
