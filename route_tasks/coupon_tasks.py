from managers.database_manager import DatabaseManager
from fastapi.exceptions import HTTPException
import logging

import re


logger = logging.getLogger(__name__)

db = DatabaseManager()

def get_coupon_data():
    resp_code, result = db.get_coupons()
    return resp_code, result


def delete_coupon(coupon_id):
    resp_code = db.delete_coupon(coupon_id)
    return resp_code

def create_coupon(request_body):
    coupon_name = request_body.get("coupon_name")
    validity = request_body.get("validity")
    resp_code= db.create_coupon(coupon_name, validity)
    return resp_code
