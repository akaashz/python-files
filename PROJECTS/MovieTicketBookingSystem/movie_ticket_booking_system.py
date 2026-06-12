import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="ak123",
    database="moviebookingsystem",
)

print("Connected Successfully!")

cursor=conn.cursor()

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100) NOT NULL
)
""")

# MOVIES TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies(
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_name VARCHAR(100) NOT NULL,
    language VARCHAR(50)
)
""")

# THEATRES TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS theatres(
    theatre_id INT AUTO_INCREMENT PRIMARY KEY,
    theatre_name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
)
""")

# SHOWS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS shows(
    show_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    theatre_id INT,
    show_date DATE,
    show_time TIME,
    ticket_price DECIMAL(10,2),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (theatre_id) REFERENCES theatres(theatre_id)
)
""")

# BOOKINGS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings(
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    show_id INT NULL,
    booking_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    seats INT,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (show_id) REFERENCES shows(show_id)
)
""")

# PAYMENTS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS payments(
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    payment_method VARCHAR(50),
    payment_status VARCHAR(20),
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
)
""")

# THEATRE SELECTION TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS theatre_selection(
    id INT AUTO_INCREMENT PRIMARY KEY,
    theatre_name VARCHAR(100),
    location VARCHAR(200),
    show_time VARCHAR(20)
)
""")

conn.commit()

print("All Tables Created Successfully!")

def register_user(conn):

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    cursor = conn.cursor()

    query = """
    INSERT INTO users(name, age, phone, email, password)
    VALUES(%s, %s, %s, %s, %s)
    """

    try:
        cursor.execute(query, (name, age, phone, email, password))
        conn.commit()
        print("Registration Successful!")

    except mysql.connector.IntegrityError:
        print("Phone number or Email already exists!")

    cursor.close()
    
def sign_in(conn):

    cursor = conn.cursor()

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    query = """
    SELECT * FROM users
    WHERE email=%s AND password=%s
    """

    cursor.execute(query, (email, password))

    user = cursor.fetchone()

    if user:
        print("Login Successful!")
        print("Welcome", user[1])
    else:
        print("Invalid Email or Password")

    cursor.close()
    
def movie_details(conn):

    cursor = conn.cursor()

    print("\n--- AVAILABLE MOVIES ---")
    print("1. The Odyssey")
    print("2. Spider-Man: Brand New Day")
    print("3. The Batman 2")
    print("4. Avengers: Secret Wars")

    choice = input("Select Movie (1-4): ")

    if choice == "1":
        movie_name = "The Odyssey"

    elif choice == "2":
        movie_name = "Spider-Man: Brand New Day"

    elif choice == "3":
        movie_name = "The Batman 2"

    elif choice == "4":
        movie_name = "Avengers: Secret Wars"

    else:
        print("Invalid Selection")
        return

    query = """
    INSERT INTO movies(movie_name)
    VALUES(%s)
    """

    cursor.execute(query, (movie_name,))
    conn.commit()

    print(movie_name, "Selected Successfully!")

    cursor.close()
    
def theatre_details(conn):

    cursor = conn.cursor()

    print("\n--- THEATRES ---")
    print("1. PVR Cinemas")
    print("2. INOX")
    print("3. KG Cinemas")
    print("4. Cinepolis")

    choice = input("Select Theatre: ")

    if choice == "1":
        theatre = "PVR Cinemas"
        location = "Brookefields Mall"

    elif choice == "2":
        theatre = "INOX"
        location = "Prozone Mall"

    elif choice == "3":
        theatre = "KG Cinemas"
        location = "Gandhipuram"

    elif choice == "4":
        theatre = "Cinepolis"
        location = "Fun Republic Mall"

    else:
        print("Invalid Selection")
        return

    print("\nShow Timings")
    print("1. 10:00 AM")
    print("2. 02:00 PM")
    print("3. 06:00 PM")
    print("4. 10:00 PM")

    t = input("Select Time: ")

    if t == "1":
        show_time = "10:00 AM"
    elif t == "2":
        show_time = "02:00 PM"
    elif t == "3":
        show_time = "06:00 PM"
    elif t == "4":
        show_time = "10:00 PM"
    else:
        print("Invalid Time")
        return

    query = """
    INSERT INTO theatre_selection(theatre_name, location, show_time)
    VALUES(%s, %s, %s)
    """

    cursor.execute(query, (theatre, location, show_time))
    conn.commit()

    print("Theatre Selected Successfully!")

    cursor.close()
    
def payment_details(conn):

    cursor = conn.cursor()

    user_id = int(input("Enter User ID: "))
    seats = int(input("Enter Number of Seats: "))

    ticket_price = 200
    amount = seats * ticket_price

    query = """
    INSERT INTO bookings(user_id, show_id, seats, total_amount)
    VALUES(%s, %s, %s, %s)
    """

    cursor.execute(query, (user_id, None, seats, amount))
    conn.commit()

    booking_id = cursor.lastrowid

    print("Booking ID:", booking_id)

    print("\n1. UPI")
    print("2. Card")
    print("3. Net Banking")

    choice = input("Select Payment Method: ")

    if choice == "1":
        payment_method = "UPI"
    elif choice == "2":
        payment_method = "Card"
    elif choice == "3":
        payment_method = "Net Banking"
    else:
        print("Invalid Choice")
        return

    query = """
    INSERT INTO payments(booking_id, payment_method, payment_status)
    VALUES(%s, %s, %s)
    """

    cursor.execute(
        query,
        (booking_id, payment_method, "Success")
    )

    conn.commit()

    print("Payment Successful!")
    print("Amount: ₹", amount)

    cursor.close()
    
def view_ticket(conn):

    cursor = conn.cursor()

    booking_id = int(input("Enter Booking ID: "))

    query = """
    SELECT
        b.booking_id,
        b.seats,
        b.total_amount,
        p.payment_method,
        p.payment_status
    FROM bookings b
    JOIN payments p
    ON b.booking_id = p.booking_id
    WHERE b.booking_id = %s
    """

    cursor.execute(query, (booking_id,))

    ticket = cursor.fetchone()

    if ticket:

        print("\n===== MOVIE TICKET =====")
        print("Booking ID :", ticket[0])
        print("Seats      :", ticket[1])
        print("Amount     : ₹", ticket[2])
        print("Method     :", ticket[3])
        print("Status     :", ticket[4])

    else:
        print("No Ticket Found")

    cursor.close()
    
while True:

    print("\n===== MOVIE TICKET BOOKING SYSTEM =====")
    print("1. Register User")
    print("2. Login")
    print("3. Movie Details")
    print("4. Theatre Details")
    print("5. Payment Details")
    print("6. View Ticket")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register_user(conn)

    elif choice == "2":
        sign_in(conn)

    elif choice == "3":
        movie_details(conn)

    elif choice == "4":
        theatre_details(conn)

    elif choice == "5":
        payment_details(conn)

    elif choice == "6":
        view_ticket(conn)

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
        





