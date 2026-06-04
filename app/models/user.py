from __future__ import annotations

from sqlalchemy import (
    String,
    Boolean
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.models.base import Base
from app.models.budget import Budget
from app.models.transaction import Transaction


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    full_name: Mapped[str] = mapped_column(
        String(100)
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True
    )

    password_hash: Mapped[str] = mapped_column(
        String
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction",
        back_populates="user"
    )

    budgets: Mapped[list["Budget"]] = relationship(
        "Budget",
        back_populates="user"
    )