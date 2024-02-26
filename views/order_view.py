import sqlite3
import json

database = "./kneeldiamonds.sqlite3"


def get_all_orders():
    with sqlite3.connect(database) as conn:
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

        ser_order = json.dumps(orders)

    return ser_order


def get_single_order(pk):
    with sqlite3.connect(database) as conn:
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
            WHERE o.id = ?
            """,
            (pk,),
        )
        query_results = db_cursor.fetchone()

    return json.dumps(dict(query_results)) if query_results else None
