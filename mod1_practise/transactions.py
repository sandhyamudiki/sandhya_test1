def greet(name):
    return f"Hello, {name}!"



def create_transaction(connection, member_id, amount, description, transaction_type = "withdrawal"):
    cursor = connection.cursor()
    cursor.execute(f"""
    INSERT INTO fi_member_transactions (member_id, amount, transaction_type, description)
    VALUES (%s, %s, %s, %s) RETURNING transaction_id ;
    """, (member_id, amount, transaction_type, description))
    connection.commit()
    id = cursor.fetchone()[0]
    print(f"Record inserted successfully!: {id}")
    return id


def retrieve_transactions(connection, member_id):
    cursor = connection.cursor()
    query = f"SELECT * FROM fi_member_transactions where member_id = {member_id} order by transaction_date desc;"
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.commit()
    for row in rows:
        print(row)
    return rows

