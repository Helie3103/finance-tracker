from datetime import date

from pydantic import BaseModel


class TransactionCreate(BaseModel):
    title: str
    amount: float
    type: str
    category_id: int
    transaction_date: date
    notes: str | None = None


class TransactionUpdate(BaseModel):
    title: str | None = None
    amount: float | None = None
    type: str | None = None
    category_id: int | None = None
    transaction_date: date | None = None
    notes: str | None = None


class TransactionResponse(BaseModel):
    id: int
    title: str
    amount: float
    type: str
    category_id: int
    transaction_date: date
    notes: str | None
    is_deleted: bool

    class Config:
        from_attributes = True