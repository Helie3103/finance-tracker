from sqlalchemy.orm import Session

from app.models.category import Category


def create_category(
    db: Session,
    name: str,
    type: str
):
    category = Category(
        name=name,
        type=type
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def get_categories(
    db: Session
):
    return (
        db.query(Category)
        .filter(Category.is_active == True)
        .all()
    )


def get_category_by_id(
    db: Session,
    category_id: int
):
    return (
        db.query(Category)
        .filter(
            Category.id == category_id,
            Category.is_active == True
        )
        .first()
    )


def update_category(
    db: Session,
    category: Category,
    name: str | None,
    type: str | None
):
    if name is not None:
        category.name = name

    if type is not None:
        category.type = type

    db.commit()
    db.refresh(category)

    return category


def delete_category(
    db: Session,
    category: Category
):
    category.is_active = False

    db.commit()

    return category

def soft_delete_category(
    db: Session,
    category: Category
):
    category.is_deleted = True

    db.commit()
    db.refresh(category)

    return category