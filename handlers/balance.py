import sqlite3

DB_FILE = "database.db"


def get_balance(user_id):

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM balances WHERE user_id=?",
        (str(user_id),)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return 0


def add_balance(user_id, amount):

    current = get_balance(user_id)

    new_balance = current + amount

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO balances
        (user_id, balance)
        VALUES (?, ?)
        """,
        (
            str(user_id),
            new_balance
        )
    )

    conn.commit()
    conn.close()

    return new_balance


def deduct_balance(user_id, amount):

    current = get_balance(user_id)

    if current < amount:
        return False

    new_balance = current - amount

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO balances
        (user_id, balance)
        VALUES (?, ?)
        """,
        (
            str(user_id),
            new_balance
        )
    )

    conn.commit()
    conn.close()

    return True
