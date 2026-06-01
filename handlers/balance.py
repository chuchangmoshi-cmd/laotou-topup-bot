import json
import os

BALANCE_FILE = "balances.json"


def load_balances():
    if not os.path.exists(BALANCE_FILE):
        return {}

    try:
        with open(BALANCE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_balances(data):
    with open(BALANCE_FILE, "w") as f:
        json.dump(data, f)


def get_balance(user_id):
    balances = load_balances()
    return balances.get(str(user_id), 0)


def add_balance(user_id, amount):
    balances = load_balances()

    user_id = str(user_id)

    balances[user_id] = balances.get(user_id, 0) + amount

    save_balances(balances)

    return balances[user_id]


def deduct_balance(user_id, amount):
    balances = load_balances()

    user_id = str(user_id)

    current = balances.get(user_id, 0)

    if current < amount:
        return False

    balances[user_id] = current - amount

    save_balances(balances)

    return True
