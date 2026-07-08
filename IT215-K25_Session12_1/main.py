from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session

from database import *
from models import *
from schema import *
from user_service import *

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.put("/products/{product_id}",response_model=UpdateProductResponse)
def handle_update_product(product_id: int,updated_product: UpdateProduct,db: Session = Depends(get_database)):
    product = update_product_service(
        product_id,
        updated_product,
        db
    )

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return UpdateProductResponse(
        message="Product updated successfully",
        data=product
    )