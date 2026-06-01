import json
import os

ORDER_FILE = "orders.json"


def load_orders():

    if not os.path.exists(ORDER_FILE):
        return {}

    try:
        with open(ORDER_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_orders(data):

    with open(ORDER_FILE, "w") as f:
        json.dump(data, f)


def add_order(user_id, order_data):

    orders = load_orders()

    user_id = str(user_id)

    if user_id not in orders:
        orders[user_id] = []

    orders[user_id].append(order_data)

    save_orders(orders)


def get_orders(user_id):

    orders = load_orders()

    return orders.get(str(user_id), [])
