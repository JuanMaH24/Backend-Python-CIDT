from models.product import Product as ProductModel
from schemas.product import Product

class ProductService():
    def __init__(self, db) -> None:
        self.db = db

    def get_products(self):
        result = self.db.query(ProductModel).all()
        return result

    def get_product(self, id:int):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return result

    def get_product_by_category(self, category):
        result = self.db.query(ProductModel).filter(ProductModel.category.like(category)).all()
        return result
    
    def get_product_by_name(self, product_name):
        result = self.db.query(ProductModel).filter(ProductModel.product_name.contains(product_name)).all()
        return result
    

    def create_product(self, product:Product):
        new_product = ProductModel(**product.model_dump())
        self.db.add(new_product)
        self.db.commit()

    def update_product(self, id:int, data:Product):
        product = self.get_product(id)
        product.product_name = data.product_name
        product.product_price = data.product_price
        product.category = data.category
        self.db.commit()

    def delete_product(self, id:int):
        product = self.get_product(id)
        self.db.delete(product)
        self.db.commit()