from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.dependencies.auth import (
    get_current_user
)

from app.models.user import User

from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse
)

from app.schemas.common import (
    MessageResponse
)

from app.services.transaction_service import (
    create_transaction,
    get_transactions,
    get_transaction_by_id,
    update_transaction,
    soft_delete_transaction
)

router = APIRouter()


@router.post(
    "/",
    response_model=TransactionResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_transaction(
    transaction_data: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_transaction(
        db,
        current_user.id,
        transaction_data
    )


@router.get(
    "/",
    response_model=list[TransactionResponse]
)
def get_all_transactions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_transactions(
        db,
        current_user.id
    )


@router.get(
    "/{transaction_id}",
    response_model=TransactionResponse
)
def get_single_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    transaction = get_transaction_by_id(
        db,
        transaction_id,
        current_user.id
    )

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction


@router.put(
    "/{transaction_id}",
    response_model=TransactionResponse
)
def update_existing_transaction(
    transaction_id: int,
    transaction_data: TransactionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    transaction = get_transaction_by_id(
        db,
        transaction_id,
        current_user.id
    )

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return update_transaction(
        db,
        transaction,
        transaction_data
    )


@router.patch(
    "/{transaction_id}/delete",
    response_model=MessageResponse
)
def remove_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    transaction = get_transaction_by_id(
        db,
        transaction_id,
        current_user.id
    )

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    soft_delete_transaction(
        db,
        transaction
    )

    return MessageResponse(
        message="Transaction deleted successfully"
    )