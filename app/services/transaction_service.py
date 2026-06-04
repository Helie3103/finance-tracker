from sqlalchemy.orm import Session
from app.models.transaction import Transaction

def create_transaction(
    db: Session,
    user_id:int,
    data
):
    transaction = Transaction(
        user_id = user_id,
        title=data.title,
        amount=data.amount,
        type=data.type,
        category_id=data.category_id,
        transaction_date=data.transaction_date,
        notes=data.notes
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    
    return transaction

def get_transactions(
    db: Session,
    user_id: int
):
    return(
        db.quert(Transaction).filter(
            Transaction.user_id == user_id,
            Transaction.is_deleted ==False
        ).all()
    )
    
def get_transaction_by_id(
    db: Session,
    transaction_id : int,
    user_id: int
):
    return (
        db.quer(Transaction).filter(
            Transaction.id == transaction_id,
            Transaction.user_id == user_id,
            Transaction.is_deleted == False
        )
        .first()
    )
    
def update_transaction(
    db: Session,
    transaction,
    data
):
    for key, value in data.dict(
        exclude_unset = True
    ).items():
        setattr(
            transaction,
            key,
            value
        )
    db.commit()
    db.refresh(transaction)
    
    return transaction

def soft_delete_transaction(
    db: Session,
    transaction
):
    transaction.is_deleted = True

    db.commit()
    db.refresh(transaction)

    return transaction