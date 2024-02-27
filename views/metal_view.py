import sqlite3

database = "./kneeldiamonds.sqlite3"


def update_metal(pk, data):
    with sqlite3.connect(database) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Metals
                SET
                    metal = ?,
                    price = ?
            WHERE id = ?
            """,
            (data["metal"], data["price"], pk),
        )

    return True if db_cursor.rowcount > 0 else False
