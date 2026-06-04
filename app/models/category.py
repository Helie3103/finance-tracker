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


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    type: Mapped[str] = mapped_column(
        String(20)
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction",
        back_populates="category"
    )

    budgets: Mapped[list["Budget"]] = relationship(
        "Budget",
        back_populates="category"
    )