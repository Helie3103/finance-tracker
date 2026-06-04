from datetime import date
from sqlalchemy import(
    String,
    Float,
    ForeignKey,
    Numeric,
    Date,
    Boolean,
    Integer,
    Column
)
from sqlalchemy.orm import(
    Mapped,
    mapped_column,
    relationship
)

from app.models.base import Base

class Transaction(Base):
    __tablename__ = "transactions"
    
    id: Mapped[int] = mapped_column(
        primary_key = True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id")
    )
    title: Mapped[str]= mapped_column(
        String(255)
    )
    amount: Mapped[float] = mapped_column(
        Numeric(12,2)
    )
    type: Mapped[str] = mapped_column(
        String(20)
    )
    transaction_date: Mapped[date] = mapped_column(
        Date
    )
    notes: Mapped[str | None] = mapped_column(
        String,
        nullable = True
    )
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default =False
    )
    user = relationship(
        "User",
        back_populates = "transactions"
    )
    category= relationship(
        "Category",
        back_populates = "transactions"
    )
   