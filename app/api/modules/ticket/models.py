from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db_utils import Base

class Ticket(Base):
    __tablename__ = "ticket"
    
    ticket_id: Mapped[int] = mapped_column(primary_key=True)
    
    wallet_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))


class TicketStops(Base):
    __tablename__ = "ticket-stops"
    
    ticket_stops_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    ticket_id: Mapped[int] = mapped_column(ForeignKey("ticket.ticket_id"))
    
    stop_id: Mapped[int] = mapped_column(ForeignKey("stop.stop_id"))
    train_id: Mapped[int] = mapped_column(ForeignKey("train.train_id"))

