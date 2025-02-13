def greet(name):
    return f"Hello, {name}!"



def create_member(connection, first_name, last_name, email:None):
    cursor = connection.cursor()
    cursor.execute(f"""
    INSERT INTO fi_members (first_name, last_name, email)
    VALUES (%s, %s, %s) RETURNING member_id ;
    """, (first_name,last_name, email))
    connection.commit()
    id = cursor.fetchone()[0]
    print(f"Record inserted successfully!: {id}")
    return id


def retrieve_members(connection, member_id=None, email=None):
    cursor = connection.cursor()
    if(member_id is None and email is None):
        query = "SELECT * FROM fi_members;"
    elif(email is None):
        query = f"SELECT * FROM fi_members where id = {member_id};"
        #query = "SELECT * FROM members where id = " + member_id
    elif(member_id is None):
        query = f"SELECT * FROM fi_members where email = '{email}';"
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.commit()
    for row in rows:
        print(row)
        print(row[0])
    return rows


def update_member(connection, member_id, first_name, last_name):
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE members
    SET first_name = %s, last_name = %s
        WHERE id = %s;
    """, (first_name, last_name, member_id))
    #connection.commit()
    print("Record updated successfully!")
    print("updated data")
    retrieve_members(connection, member_id)


def delete_member(connection, member_id):
    cursor = connection.cursor()
    cursor.execute(f"""
    DELETE FROM members
    WHERE id = {member_id};
    """)
    connection.commit()
    print("Record deleted successfully!")