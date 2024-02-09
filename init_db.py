from app.db_utils import Base, engine

# Import the models to create the tables

# For example, if we have a books module with a Book model
# from app.api.modules.books.model import Book
from app.api.modules.user.models import User
from app.api.modules.station.models import Station
from app.api.modules.train.models import Train, Stops
from app.api.modules.ticket.models import Ticket, TicketStops

if __name__ == "__main__":

    Base.metadata.create_all(bind=engine)
    print("Database initialized!")
