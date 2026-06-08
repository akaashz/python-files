import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ak123",
    database="pythontraaining"
)

print("Connected successfully!")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15)
)
""")

conn.commit()
cursor.close()


def register_user(conn):
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    phone_number = input("Enter phone number: ")

    cursor = conn.cursor()

    query = """
    INSERT INTO users (username, password, email, phone_number)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (username, password, email, phone_number))
    conn.commit()

    print("User registered successfully!")
    cursor.close()


def update_password(conn):
    username = input("Enter Username: ")
    new_password = input("Enter New Password: ")

    cursor = conn.cursor()

    query = """
    UPDATE users
    SET password = %s
    WHERE username = %s
    """

    cursor.execute(query, (new_password, username))
    conn.commit()

    if cursor.rowcount > 0:
        print("Password updated successfully!")
    else:
        print("User not found!")

    cursor.close()

def update_email(conn):
    username = input("Enter Username: ")
    new_email = input("Enter New Email: ")

    cursor = conn.cursor()

    query = """
    UPDATE users
    SET email = %s
    WHERE username = %s
    """

    cursor.execute(query, (new_email, username))
    conn.commit()

    if cursor.rowcount > 0:
        print("Email updated successfully!")
    else:
        print("User not found!")

    cursor.close()
    
def delete_user(conn):
    username=input("Enter user to delete = ")
    cursor=conn.cursor()
    query = """
    DELETE FROM users
    WHERE username = %s
    """
    cursor.execute(query,(username,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print("User deleted succesfully !")
    else:
        print("User not found!")
        
    cursor.close()

def view_user(conn):
    username=input("Enter your user to view : ")
    cursor=conn.cursor()
    query = """
    SELECT id, username, email, phone_number
    FROM users
    WHERE username = %s
    """
    cursor.execute(query,(username,))
    user = cursor.fetchone()
    
    if user:
        print("\nUser Details")
        print("ID:", user[0])
        print("Username:", user[1])
        print("Email:", user[2])
        print("Phone Number:", user[3])
    else:
        print("User not found!")

    cursor.close()
    
        


# Menu Loop
while True:
    print("\n1. Register User")
    print("2. Update Password")
    print("3. Update Email")
    print("4. Delete User")
    print("5. View user")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register_user(conn)

    elif choice == "2":
        update_password(conn)
    
    elif choice == "3":
        update_email(conn)
    
    elif choice == "4":
        delete_user(conn)

    elif choice == "5":
        view_user(conn)   
        
    elif choice == "6":
        break  

    else:
        print("Invalid choice!")


