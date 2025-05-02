from flask import Blueprint, request, jsonify
from models.product import Product
from models.stock import Stock
from extensions import db

stock_bp = Blueprint("stock_bp", __name__)

@stock_bp.route("/stock", methods=["GET"])
def get_all():
    movements = Stock.query.all()
    return jsonify()