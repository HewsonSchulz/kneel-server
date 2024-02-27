import sqlite3
import json

database = './kneeldiamonds.sqlite3'


def get_all_orders():
    with sqlite3.connect(database) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            '''
            SELECT
                o.id,
                o.timestamp,
                o.styleId,
                st.style,
                st.price style_price,
                o.sizeId,
                s.carets,
                s.price size_price,
                o.metalId,
                m.metal,
                m.price metal_price
            FROM Orders o
            JOIN Styles st ON st.id = o.styleId
            JOIN Sizes s ON s.id = o.sizeId
            JOIN Metals m ON m.id = o.metalId;
            '''
        )
        query_results = db_cursor.fetchall()

        orders = []

        for row in query_results:
            style = {
                'style': row['style'],
                'price': row['style_price'],
            }
            size = {
                'carets': row['carets'],
                'price': row['size_price'],
            }
            metal = {
                'metal': row['metal'],
                'price': row['metal_price'],
            }
            order = {
                'id': row['id'],
                'timestamp': row['timestamp'],
                'styleId': row['styleId'],
                'style': style,
                'sizeId': row['sizeId'],
                'size': size,
                'metalId': row['metalId'],
                'metal': metal,
            }
            orders.append(order)

        ser_order = json.dumps(orders)

    return ser_order


def get_single_order(pk):
    with sqlite3.connect(database) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            '''
            SELECT
                o.id,
                o.timestamp,
                o.styleId,
                st.style,
                st.price style_price,
                o.sizeId,
                s.carets,
                s.price size_price,
                o.metalId,
                m.metal,
                m.price metal_price
            FROM Orders o
            JOIN Styles st ON st.id = o.styleId
            JOIN Sizes s ON s.id = o.sizeId
            JOIN Metals m ON m.id = o.metalId
            WHERE o.id = ?
            ''',
            (pk,),
        )

        query_results = db_cursor.fetchone()

        if query_results:
            style = {
                'style': query_results['style'],
                'price': query_results['style_price'],
            }
            size = {
                'carets': query_results['carets'],
                'price': query_results['size_price'],
            }
            metal = {
                'metal': query_results['metal'],
                'price': query_results['metal_price'],
            }
            order = {
                'id': query_results['id'],
                'timestamp': query_results['timestamp'],
                'styleId': query_results['styleId'],
                'style': style,
                'sizeId': query_results['sizeId'],
                'size': size,
                'metalId': query_results['metalId'],
                'metal': metal,
            }
            return json.dumps(order)

    return None


def create_order(data):
    with sqlite3.connect(database) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            '''
            INSERT INTO Orders
            (timestamp, styleId, sizeId, metalId)
            VALUES (?, ?, ?, ?)
            ''',
            (data['timestamp'], data['styleId'], data['sizeId'], data['metalId']),
        )

        order_id = db_cursor.lastrowid

        # retrieve the newly created order
        db_cursor.execute(
            '''
            SELECT
                o.id,
                o.timestamp,
                o.styleId,
                o.sizeId,
                o.metalId
            FROM Orders o
            WHERE o.id = ?
            ''',
            (order_id,),
        )
        new_order = db_cursor.fetchone()

        order_dict = {
            'id': new_order[0],
            'timestamp': new_order[1],
            'styleId': new_order[2],
            'sizeId': new_order[3],
            'metalId': new_order[4],
        }

    return order_dict if order_dict else None


def delete_order(pk):
    with sqlite3.connect(database) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            '''
            DELETE FROM Orders WHERE id = ?
            ''',
            (pk,),
        )
        number_of_rows_deleted = db_cursor.rowcount

    return True if number_of_rows_deleted > 0 else False
