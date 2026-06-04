from __future__ import annotations

from sqlalchemy import (
    ForeignKey,
    Integer,
    Numeric,
    Boolean
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.models.base import Base


class Budget(Base):
    __tablename__ = "budgets"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id")
    )

    amount: Mapped[float] = mapped_column(
        Numeric(12, 2)
    )

    year: Mapped[int] = mapped_column(
        Integer
    )

    month: Mapped[int] = mapped_column(
        Integer
    )

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    user = relationship(
        "User",
        back_populates="budgets"
    )

    category = relationship(
        "Category",
        back_populates="budgets"
    )