from extensions import db
from datetime import datetime

class Stock(db.Model):
    __tablename__ = "stock"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, product_id, type, quantity):
        self.product_id = product_id
        self.type = type
        self.quantity = quantity

        def to_dict(self):
            return {
                "id": self.id,
                "product_id": self.product_id,
                "type": self.type,
                "quantity": self.quantity,
                "date": self.date.strftime('%Y-%m-%d %H:%M:%S')
            }
        