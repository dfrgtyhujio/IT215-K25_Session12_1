from pydantic import BaseModel, ConfigDict


class UpdateProduct(BaseModel):
    name: str
    price: float


class ProductResponse(BaseModel):
    id: int
    sku: str
    name: str
    price: float

    model_config = ConfigDict(from_attributes=True)


class UpdateProductResponse(BaseModel):
    message: str
    data: ProductResponse