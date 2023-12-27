import mysql.connector
def connect_to_database():
    # Replace the placeholders with your MySQL database credentials
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '12345678',
        'database': 'students',
        'raise_on_warnings': True
    }

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            print("Connected to the MySQL database")
            return connection

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

def query_all_rows(connection,table_name):
    try:

        cursor = connection.cursor()

        # Execute a simple query to fetch all rows from the specified table
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Display the results
        print(f"\nAll rows from {table_name} table:")
        for row in rows:
            print(row)

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        print("Connection closed.")

def insert_new_row(connection,table_name):
    id = int(input("Please Enter ID: "))
    fullname = input("Please Enter Fullname: ")
    major = input("Please Enter Major: ")
    gpa = float(input("Please Enter GPA: "))
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO {table_name} (id, fullname, major, gpa) VALUE ({id}, '{fullname}', '{major}', {gpa})"
        cursor.execute(query)
        connection.commit()
    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        print("Insert Complete!")
        print("Connection closed.")
def select_updata_table(connection,table_name):
    print("Which column do you want to update?")
    print("choose 1 : ID")
    print("choose 2 : fullname")
    print("choose 3 : major")
    print("choose 4 : gap")
    choose = int(input("Please select :"))
    if choose == 1:
        new_id = int(input("Please Enter new ID: "))
        update_table(connection, table_name, "id", new_id, where=int(input("Where ID? : ")))
    elif choose == 2:
        new_fullname = input("Please Enter new Fullname: ")
        update_table(connection, table_name, "fullname", new_fullname, where=int(input("Where ID? : ")))
    elif choose == 3:
        new_major = input("Please Enter new Major: ")
        update_table(connection, table_name, "major", new_major, where=int(input("Where ID? : ")))
    elif choose == 4:
        new_gpa = float(input("Please Enter new GPA: "))
        update_table(connection, table_name, "gpa", new_gpa, where=int(input("Where ID? : ")))
        
def update_table(connection, table_name, column_name, new_value, where):
    try:
        cursor = connection.cursor()
        query = f"UPDATE {table_name} SET {column_name} = %s WHERE id = %s"
        values = (new_value, where)
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        print("Update Complete!")
        print("Connection closed.")
def delete_row(connection, table_name):
    where = int(input("Where ID? : "))
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM {table_name} WHERE id = %s"
        values = (where,)  # Note the comma to create a tuple
        cursor.execute(query, values)
        connection.commit()
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        print("Delete Complete!")
        print("Connection closed.")
connection=connect_to_database()
while(True):
    print("====MENU====")
    print("1: show all rows")
    print("2: insert a new row")
    print("3: update specific row")
    print("4: delete specific row")
    print("5: exit")
    choice=input("Please choose: ")

    if int(choice)==1:
        if connection:
            query_all_rows(connection,"std_info")
    elif int(choice)==2:
            insert_new_row(connection,"std_info")
    elif int(choice)==3:
            select_updata_table(connection,"std_info")      
    elif int(choice)==4:
            delete_row(connection,"std_info")
    elif int(choice)==5:
            print("Bye Bye")
            break

connection.close()
