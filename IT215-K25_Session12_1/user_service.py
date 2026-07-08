from models import *
from schema import *
from sqlalchemy.orm import Session


def update_product_service(product_id: int, updated_product: UpdateProduct, db: Session):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if not product:
        return None

    product.name = updated_product.name
    product.price = updated_product.price

    db.commit()
    db.refresh(product)

    return product