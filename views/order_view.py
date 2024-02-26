import sqlite3
import json


def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                o.id,
                o.styleId,
                o.sizeId,
                o.metalId,
                o.typeId
            FROM Orders o
            """
        )
        query_results = db_cursor.fetchall()

        orders = []
        for row in query_results:
            orders.append(dict(row))

        ser_out = json.dumps(orders)

    return ser_out


def get_single_order(pk):
    pass  #!
